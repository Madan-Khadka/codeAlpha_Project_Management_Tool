/*
============================================================
PROJECT MANAGEMENT TOOL - MAIN JAVASCRIPT
============================================================

This file handles:

1. Mobile/menu interactions
2. Create Task modal
3. Drag and drop task cards
4. Task count
5. CSRF token handling
6. AJAX task status update
7. Basic notifications
8. Confirmation messages
============================================================
*/


/* =========================================================
   RUN JAVASCRIPT AFTER PAGE LOAD
   ========================================================= */

document.addEventListener("DOMContentLoaded", function () {

    /*
     * Initialize all project management features.
     */
    initializeTaskModal();
    initializeDragAndDrop();
    updateTaskCounts();
    initializeConfirmations();
    initializeMobileMenu();

});


/* =========================================================
   CREATE TASK MODAL
   ========================================================= */

function initializeTaskModal() {

    /*
     * Find modal elements.
     */
    const modal = document.getElementById("taskModal");
    const openButton = document.getElementById("openTaskModal");

    const closeButton = document.getElementById("closeTaskModalButton");
    const cancelButton = document.getElementById("cancelTaskButton");

    const overlay = document.getElementById("closeTaskModal");


    /*
     * If modal does not exist,
     * stop the function.
     */
    if (!modal) {
        return;
    }


    /*
     * Open modal.
     */
    if (openButton) {

        openButton.addEventListener("click", function () {

            modal.classList.add("active");

            modal.setAttribute("aria-hidden", "false");

            /*
             * Automatically focus task title.
             */
            const titleInput = document.getElementById("id_title");

            if (titleInput) {
                setTimeout(function () {
                    titleInput.focus();
                }, 100);
            }

        });

    }


    /*
     * Close modal using X button.
     */
    if (closeButton) {

        closeButton.addEventListener("click", function () {

            closeTaskModal();

        });

    }


    /*
     * Close modal using Cancel button.
     */
    if (cancelButton) {

        cancelButton.addEventListener("click", function () {

            closeTaskModal();

        });

    }


    /*
     * Close modal by clicking outside.
     */
    if (overlay) {

        overlay.addEventListener("click", function () {

            closeTaskModal();

        });

    }


    /*
     * Close modal using ESC key.
     */
    document.addEventListener("keydown", function (event) {

        if (event.key === "Escape") {

            closeTaskModal();

        }

    });

}


/*
 * Function to close task modal.
 */
function closeTaskModal() {

    const modal = document.getElementById("taskModal");

    if (!modal) {
        return;
    }

    modal.classList.remove("active");

    modal.setAttribute("aria-hidden", "true");

}


/* =========================================================
   DRAG AND DROP
   ========================================================= */

function initializeDragAndDrop() {

    /*
     * Select all task cards.
     */
    const taskCards = document.querySelectorAll(".task-card");

    /*
     * Select all board columns.
     */
    const taskLists = document.querySelectorAll(".task-list");


    /*
     * Add drag events to every task card.
     */
    taskCards.forEach(function (card) {

        card.addEventListener("dragstart", function (event) {

            /*
             * Store task ID while dragging.
             */
            const taskId = card.dataset.taskId;

            event.dataTransfer.setData(
                "text/plain",
                taskId
            );

            /*
             * Add visual effect.
             */
            card.classList.add("dragging");

        });


        card.addEventListener("dragend", function () {

            /*
             * Remove visual effect.
             */
            card.classList.remove("dragging");

        });

    });


    /*
     * Allow task cards to be dropped
     * inside another column.
     */
    taskLists.forEach(function (list) {

        list.addEventListener("dragover", function (event) {

            event.preventDefault();

            list.classList.add("drag-over");

        });


        list.addEventListener("dragleave", function () {

            list.classList.remove("drag-over");

        });


        list.addEventListener("drop", function (event) {

            event.preventDefault();

            list.classList.remove("drag-over");


            /*
             * Get task ID.
             */
            const taskId =
                event.dataTransfer.getData("text/plain");


            /*
             * Get new status.
             */
            const newStatus =
                list.dataset.status;


            /*
             * Find dragged task.
             */
            const taskCard =
                document.querySelector(
                    `.task-card[data-task-id="${taskId}"]`
                );


            /*
             * Move card visually.
             */
            if (taskCard) {

                list.appendChild(taskCard);

                /*
                 * Update task status in backend.
                 */
                updateTaskStatus(
                    taskId,
                    newStatus
                );

                /*
                 * Update task counters.
                 */
                updateTaskCounts();

            }

        });

    });

}


/* =========================================================
   UPDATE TASK STATUS
   ========================================================= */

/*
 * Sends task status update to Django backend.
 *
 * IMPORTANT:
 * This expects your Django backend to provide
 * an endpoint similar to:
 *
 * /tasks/<task_id>/update-status/
 *
 */
function updateTaskStatus(taskId, newStatus) {

    /*
     * Get CSRF token.
     */
    const csrfToken = getCSRFToken();


    /*
     * If CSRF token is missing,
     * don't send the request.
     */
    if (!csrfToken) {

        showNotification(
            "Security token missing. Please refresh the page.",
            "error"
        );

        return;

    }


    /*
     * Send POST request to Django.
     */
    fetch(`/tasks/${taskId}/update-status/`, {

        method: "POST",

        headers: {

            "Content-Type": "application/json",

            "X-CSRFToken": csrfToken,

            "X-Requested-With": "XMLHttpRequest"

        },

        body: JSON.stringify({

            status: newStatus

        })

    })


    /*
     * Convert response to JSON.
     */
    .then(function (response) {

        if (!response.ok) {

            throw new Error(
                "Unable to update task."
            );

        }

        return response.json();

    })


    /*
     * Handle successful response.
     */
    .then(function (data) {

        if (data.success) {

            showNotification(
                "Task status updated successfully.",
                "success"
            );

        } else {

            showNotification(
                data.message || "Task update failed.",
                "error"
            );

        }

    })


    /*
     * Handle errors.
     */
    .catch(function (error) {

        console.error(
            "Task status error:",
            error
        );


        showNotification(
            "Could not update task status.",
            "error"
        );

    });

}


/* =========================================================
   TASK COUNTS
   ========================================================= */

function updateTaskCounts() {

    /*
     * Get each task list.
     */
    const todoTasks =
        document.querySelectorAll(
            "#todoTasks .task-card"
        );

    const progressTasks =
        document.querySelectorAll(
            "#progressTasks .task-card"
        );

    const doneTasks =
        document.querySelectorAll(
            "#doneTasks .task-card"
        );


    /*
     * Update individual counters.
     */
    const todoCount =
        document.getElementById("todoCount");

    const progressCount =
        document.getElementById("progressCount");

    const doneCount =
        document.getElementById("doneCount");


    if (todoCount) {

        todoCount.textContent =
            todoTasks.length;

    }


    if (progressCount) {

        progressCount.textContent =
            progressTasks.length;

    }


    if (doneCount) {

        doneCount.textContent =
            doneTasks.length;

    }


    /*
     * Update total task count.
     */
    const totalTasks =
        document.getElementById("totalTasks");


    if (totalTasks) {

        totalTasks.textContent =
            todoTasks.length +
            progressTasks.length +
            doneTasks.length;

    }

}


/* =========================================================
   CSRF TOKEN
   ========================================================= */

/*
 * Django requires a CSRF token
 * for POST requests.
 */
function getCSRFToken() {

    /*
     * Search browser cookies.
     */
    const cookies =
        document.cookie.split(";");


    /*
     * Find csrftoken cookie.
     */
    for (let i = 0; i < cookies.length; i++) {

        const cookie =
            cookies[i].trim();


        if (
            cookie.startsWith("csrftoken=")
        ) {

            return decodeURIComponent(
                cookie.substring(
                    "csrftoken=".length
                )
            );

        }

    }


    /*
     * Return null if token
     * was not found.
     */
    return null;

}


/* =========================================================
   NOTIFICATION SYSTEM
   ========================================================= */

/*
 * Displays temporary notification messages.
 *
 * type:
 * - success
 * - error
 * - warning
 */
function showNotification(message, type = "success") {

    /*
     * Create notification element.
     */
    const notification =
        document.createElement("div");


    /*
     * Add CSS classes.
     */
    notification.className =
        `notification notification-${type}`;


    /*
     * Add message.
     */
    notification.textContent =
        message;


    /*
     * Add notification to page.
     */
    document.body.appendChild(
        notification
    );


    /*
     * Small delay allows CSS animation
     * to work properly.
     */
    setTimeout(function () {

        notification.classList.add(
            "show"
        );

    }, 10);


    /*
     * Automatically remove after 3 seconds.
     */
    setTimeout(function () {

        notification.classList.remove(
            "show"
        );


        setTimeout(function () {

            notification.remove();

        }, 300);

    }, 3000);

}


/* =========================================================
   CONFIRMATION BUTTONS
   ========================================================= */

/*
 * Handles buttons that contain:
 *
 * data-confirm="Are you sure?"
 *
 */
function initializeConfirmations() {

    const confirmButtons =
        document.querySelectorAll(
            "[data-confirm]"
        );


    confirmButtons.forEach(function (button) {

        button.addEventListener(
            "click",
            function (event) {

                const message =
                    button.dataset.confirm;


                /*
                 * Stop action if user cancels.
                 */
                if (!confirm(message)) {

                    event.preventDefault();

                }

            }
        );

    });

}


/* =========================================================
   MOBILE MENU
   ========================================================= */

function initializeMobileMenu() {

    /*
     * Common IDs used for mobile navigation.
     */
    const menuButton =
        document.getElementById("menuToggle");

    const navigation =
        document.getElementById("mobileMenu");


    /*
     * If mobile menu doesn't exist,
     * don't do anything.
     */
    if (!menuButton || !navigation) {

        return;

    }


    /*
     * Toggle mobile navigation.
     */
    menuButton.addEventListener(
        "click",
        function () {

            navigation.classList.toggle(
                "active"
            );

        }
    );

}


/* =========================================================
   DELETE TASK CONFIRMATION
   ========================================================= */

/*
 * Can be used by task detail page.
 */
function confirmTaskDelete() {

    return confirm(
        "Are you sure you want to delete this task?"
    );

}


/* =========================================================
   DELETE PROJECT CONFIRMATION
   ========================================================= */

/*
 * Can be used by project page/dashboard.
 */
function confirmProjectDelete() {

    return confirm(
        "Are you sure you want to delete this project?"
    );

}


/* =========================================================
   AUTO HIDE DJANGO MESSAGES
   ========================================================= */

/*
 * Django messages can have:
 *
 * success
 * error
 * warning
 * info
 *
 * This function automatically hides them.
 */
function initializeDjangoMessages() {

    const messages =
        document.querySelectorAll(
            ".alert"
        );


    messages.forEach(function (message) {

        setTimeout(function () {

            message.style.opacity = "0";

            setTimeout(function () {

                message.remove();

            }, 500);

        }, 4000);

    });

}


/*
 * Initialize Django messages.
 */
document.addEventListener(
    "DOMContentLoaded",
    initializeDjangoMessages
);


/* =========================================================
   REAL-TIME UPDATE PREPARATION
   ========================================================= */

/*
 * This function prepares the project for
 * WebSocket support.
 *
 * Later you can connect this with Django Channels.
 */
function initializeWebSocket(projectId) {

    /*
     * Don't start WebSocket if project ID
     * is not available.
     */
    if (!projectId) {

        return;

    }


    /*
     * Select WebSocket protocol.
     *
     * HTTPS -> wss://
     * HTTP  -> ws://
     */
    const protocol =
        window.location.protocol === "https:"
            ? "wss"
            : "ws";


    /*
     * WebSocket URL.
     *
     * This endpoint will be handled by
     * Django Channels later.
     */
    const socketURL =
        `${protocol}://${window.location.host}/ws/projects/${projectId}/`;


    /*
     * Create WebSocket connection.
     *
     * NOTE:
     * This only works after Django Channels
     * and routing are configured.
     */
    try {

        const socket =
            new WebSocket(socketURL);


        /*
         * WebSocket connected.
         */
        socket.onopen = function () {

            console.log(
                "WebSocket connected."
            );

        };


        /*
         * Receive real-time message.
         */
        socket.onmessage = function (event) {

            try {

                const data =
                    JSON.parse(event.data);


                console.log(
                    "Real-time update:",
                    data
                );


                /*
                 * Example:
                 * Refresh task counters
                 * after receiving update.
                 */
                updateTaskCounts();


            } catch (error) {

                console.error(
                    "Invalid WebSocket data:",
                    error
                );

            }

        };


        /*
         * WebSocket error.
         */
        socket.onerror = function (error) {

            console.error(
                "WebSocket error:",
                error
            );

        };


        /*
         * WebSocket closed.
         */
        socket.onclose = function () {

            console.log(
                "WebSocket connection closed."
            );

        };


        /*
         * Return socket so other code
         * can use it.
         */
        return socket;

    } catch (error) {

        console.error(
            "WebSocket initialization failed:",
            error
        );

    }

}


/* =========================================================
   END OF MAIN.JS
   ========================================================= */