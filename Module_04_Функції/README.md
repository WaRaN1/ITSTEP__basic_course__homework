# _Модуль 4. Функції_

- ## __Завдання №1__
  - ### __1.1__
    Є три кортежі цілих чисел, необхідно знайти елементи, які є у всіх кортежах
  
  - ### __1.2__
    Є три кортежі цілих чисел, необхідно знайти елементи, які є унікальними для кожного списку

  - ### __1.3__
    Є три кортежі цілих чисел, необхідно знайти елементи, які є у кожному з кортежей та знаходяться у кожному з кортежів на тих же позиціях

- ## __Завдання №2__
  - ### __2.1__
    ### Здати багаж до камери схову
    На вхід програмиподаються данні про пасажирів, що бажають здати свій багаж до камери схову на завчасно
    відомий час до опівночі. 
    - У першій строці повідомляється число пасажирів *N*, яке не менше 3, але не перевищує 1000;
    - У другій строці - кількість чарунок у камері схову *К*, яке не менше 10, але не первищує 1000.
    #### 
    Кожна з наступних *N* має наступний  формат:
    #### <Фамілія> <час здачі багажу> <час звільнення чарунки>,
    - де
      - <Фамілія> - строка, що складаєтьсяне більше ніж з 20 непробільних символів:
      - <Час здачі багажу> - через двокрапку два цілих числа, що відповідають годинам (від 00 до 23 - рівно 2 символа) та хвилинам (від 00 до 59 - рівно 2 символи);
      - <Час звільнення чарунки> - має той же формат
      - <Фамілія> та <час здачі багажу>, а також <час здачі багажу> та <час звільнення чарунки> розділені одним пробілом.
      - Час звільнення більше часу здачі.
      - Відомості відсортовані у порядку часу здачі багажу.
      - Кожному з пасажирів у камері схову виділяється вільна чарунка з мінімальним номером.
Якщо у момент здача багажу вільних камер немає, то пасажир йде, не очікуючи звільнення однієї з них
    ######
    Необхідно написати програму, яка буде виводити на екран для кожного пасажира номер наданої йому камери (можна
одразу після введення данних пасажира). Якщо камери пасажиру не надано, то його фамілія не друкується. 

- ## __Завдання №3__
  - ### __3.1__
    При заданій цілій кількості n порахуйте n + nn + nnn.
  - ### __3.2__
    Напишіть функцію, яка приймає два числа як параметрі відображає усі парні числа між ними.

- ## __Завдання №4__
  - ### __4.1__
    Припустимо, що у нас є список клієнтів і нам для
    заданого клієнта потрібно вивести його позиції у списку
    та підрахувати, скільки разів він зустрічається у списку,
    тобто, для частих клієнтів (тих, хто зустрічається у списку
    більше одного разу) діє деяка знижка.
  ##### 
     Створимо функцію, яка виводить позиції елементів
     (клієнтів) у списку та підраховує (повертає) кількість
     входжень.
  ##### 
    В основному коді використовуємо результат роботи
    цієї функції для визначення ситуації, чи буде знижка для
    цього клієнта.

- ## __Завдання №5__
  - ### __5.1__
    Функція визначення кількості голосних у рядку.
    На вході маємо рядок з буква латинського алвафіту.
  - ### __5.2__
    Напишіть функцію, яка виводить на екран формато-ваний текст, наведений нижче:
  #####
          “Don’t let the noise of others’ opinions
          drown out your own inner voice.”
                                        Steve Jobs
  - ### __5.3__
    Напишіть функцію, яка перевіряє чи є шестизначне
    число «щасливим». Число передається як параметр.
    Якщо число щасливе, поверніть з функції _true_, якщо
    ні — _false_.
  ##### 
     «Щасливе шестизначне число» — це число, в якому
     сума перших трьох цифр дорівнює сумі других трьох
     цифр. Наприклад, 123420 — щасливе 1+2+3 = 4+2+0, а
     723422 — нещасливе 7+2+3 != 4+2+2.