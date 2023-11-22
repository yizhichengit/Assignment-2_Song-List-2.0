# CP1404 Assignment 2 - Song List 2.0 by Yizhi Chen

A Python project with GUI and Console programs that (re)use classes to manage a list of songs to learn.

# Project Reflection

## 1. How long did the entire project (assignment 2) take you?

...It took me about ten hours to complete this project, and I divided it into two parts to complete.

## 2. What are you most satisfied with?

...What I am most satisfied with is that my code has implemented all the functions required by the homework, and my layout is also very consistent with what the teacher gave me.

## 3. What are you least satisfied with?

...The entire project took too long, and when the program reported an error, it was difficult to find the problem.

## 4. What worked well in your development process?

...The class worked well.

## 5. What about your process could be improved the next time you do a project like this?

...Of course, I can improve my process. I think I should first complete the class, then complete the layout, and finally write the main program.

## 6. Describe what learning resources you used and how you used them.

...i use the guitars.py,spinner_demo.py,dynamic_widgets.py and their .kv file，And then I searched a lot of information on Google.

## 7. Describe the main challenges or obstacles you faced and how you overcame them.

1. **Understanding Kivy's Event-Driven Architecture:**
   - Kivy operates on an event-driven architecture, which can be non-intuitive for developers accustomed to procedural or synchronous code. To manage this, it's important to spend time with the Kivy documentation and tutorials, and to practice creating small, focused applications to understand how events and callbacks work within the framework.

2. **Managing the App Lifecycle:**
   - Ensuring that data is saved when the app closes is a common issue. Overcoming this involves hooking into the app's lifecycle events, such as `on_stop`, and ensuring that the `save_songs` function is called at the right time.

3. **Dynamic UI Updates:**
   - Updating the UI dynamically based on user interactions or background processes can be challenging. This can be addressed by using Kivy properties (like `StringProperty`, `ListProperty`, etc.) which automatically update the UI when their values change.

4. **Data Persistence:**
   - Saving and loading data (like the song list) correctly can be tricky. To ensure data integrity, it's important to handle file operations with care, using proper exception handling and ensuring that files are closed properly after operations are completed.

5. **UI Responsiveness:**
   - Keeping the UI responsive during long-running tasks requires understanding of threading or asynchronous programming. Overcoming this might involve using Kivy's `Clock` class or Python's threading module to run tasks in the background.

6. **Layout and Styling:**
   - Achieving the desired layout and styling can be difficult, especially when the app is scaled to different screen sizes. Using Kivy's size and position hints, as well as understanding the different layout classes, can help create a responsive design.

7. **Error Handling and Validation:**
   - User input validation and error handling are crucial for a good user experience. Implementing robust form validation and providing clear user feedback can help prevent and handle errors gracefully.

## 8. Briefly describe your experience using classes and if/how they improved your code.

...Using classes (the foundation of object-oriented programming) in programming can improve the organization and reusability of code. Classes allow for encapsulating relevant data and functionality together, making the code more modular, easy to understand, and maintain. For example, in the Kivy application project, classes can represent songs ('Song ') and song collections ('SongCollection'), and each class encapsulates relevant data and operations. This not only makes the code clearer, but also facilitates the extension and reuse of functions.
