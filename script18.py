# """წყარო — დავალება (3).odt | Thread-ები და პროცესები"""
#
# import time
# import threading
# import multiprocessing
#
#
# # სავარჯიშო 1 — ჩაის მომზადება
# def make_tea(name, seconds):
#     print(f"{name}: იწყება")
#     time.sleep(seconds)
#     print(f"{name}: მზადაა")
#
#
# teas = [
#     ("მწვანე ჩაი", 1.0),
#     ("შავი ჩაი", 1.5),
#     ("ბალახის ჩაი", 2.0),
# ]
#
#
# def compare_tea():
#     start = time.perf_counter()
#     for name, seconds in teas:
#         make_tea(name, seconds)
#     sequential_time = time.perf_counter() - start
#     print(f"თანმიმდევრულად: {sequential_time:.1f} წმ")
#
#     start = time.perf_counter()
#     threads = []
#     for name, seconds in teas:
#         thread = threading.Thread(target=make_tea, args=(name, seconds))
#         threads.append(thread)
#         thread.start()
#
#     # ჯერ ყველა thread გავუშვით, შემდეგ თითოეულს დასრულებას ველოდებით.
#     for thread in threads:
#         thread.join()
#
#     threaded_time = time.perf_counter() - start
#     print(f"thread-ებით: {threaded_time:.1f} წმ")
#     print(f"დაჩქარება: {sequential_time / threaded_time:.1f}x")
#
#
# # Thread-ები დაახლოებით 2 წამში ასრულებენ სამუშაოს,
# # რადგან time.sleep-ით ლოდინი პარალელურად მიმდინარეობს
# # და საერთო დრო ყველაზე ხანგრძლივ ლოდინზეა დამოკიდებული.
#
#
# # სავარჯიშო 2 — სამი გზა და შედარება
# def cpu_task(n):
#     while n > 0:
#         n -= 1
#
#
# def io_task(seconds):
#     time.sleep(seconds)
#
#
# def run_sequential(task, jobs):
#     for job in jobs:
#         task(job)
#
#
# def run_threads(task, jobs):
#     threads = []
#     for job in jobs:
#         thread = threading.Thread(target=task, args=(job,))
#         threads.append(thread)
#         thread.start()
#
#     for thread in threads:
#         thread.join()
#
#
# def run_processes(task, jobs):
#     processes = []
#     for job in jobs:
#         process = multiprocessing.Process(target=task, args=(job,))
#         processes.append(process)
#         process.start()
#
#     for process in processes:
#         process.join()
#
#
# def measure(runner, task, jobs):
#     start = time.perf_counter()
#     runner(task, jobs)
#     return time.perf_counter() - start
#
#
# def compare_methods(task_name, task, jobs):
#     sequential = measure(run_sequential, task, jobs)
#     threaded = measure(run_threads, task, jobs)
#     processed = measure(run_processes, task, jobs)
#
#     print(
#         f"{task_name:<10} | "
#         f"{sequential:.2f} წმ (1.0x) | "
#         f"{threaded:.2f} წმ ({sequential / threaded:.1f}x) | "
#         f"{processed:.2f} წმ ({sequential / processed:.1f}x)"
#     )
#
#
# # CPU-bound ამოცანა Python-ის ჩვეულებრივი thread-ებით არ ჩქარდება
# # GIL-ის გამო: ერთ მომენტში Python-ის ბაიტკოდს მხოლოდ ერთი thread ასრულებს.
# # I/O-bound ამოცანა ჩქარდება, რადგან time.sleep-ის დროს thread ლოდინშია,
# # ხოლო სხვა thread-ებს ამ დროს მუშაობა შეუძლიათ.
#
#
# if __name__ == "__main__":
#     compare_tea()
#
#     print()
#     print("ტიპი       | თანმიმდევრულად     | thread-ები           | პროცესები")
#     print("-" * 76)
#
#     cpu_jobs = [10_000_000] * 4
#     io_jobs = [1.0] * 4
#
#     compare_methods("CPU-bound", cpu_task, cpu_jobs)
#     compare_methods("I/O-bound", io_task, io_jobs)
#
#     # multiprocessing.Process Windows-ზე სწორად მუშაობისთვის
#     # __main__ ბლოკიდან უნდა გამოიძახოთ.
