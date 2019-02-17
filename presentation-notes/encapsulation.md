Encapsulation
=============
            
The idea of *encapsulation* is fundamental to computers in a number of ways. Generally speaking, "encapsulation" refers to the idea of building a container around something, as if that thing were contained in a capsule. When it comes to computers, there are a couple of slightly different ways the term might be used.

Hiding code in a class, function, or library
--------------------------------------------

Commonly in computer programming, *encapsulation* refers to the idea of hiding away the details of code. For example, you may write a bit of Python code that takes three coefficients for a quadratic equation `a`, `b`, and `c`, and calculates the real roots (solutions) of that equation:


    a = 2
    b = 4
    c = -5
    root1 = (-b + ((b * b) - (4 * a * c)) ** (1 / 2)) / (2 * a)
    root2 = (-b - ((b * b) - (4 * a * c)) ** (1 / 2)) / (2 * a)

If you were having to write lots of programs to calculate quadratic roots, or if you wanted to be able to use those lines of code other places, you might very well write them into a small function, class, or program that you could use in lots of different places. You might call that function like this:

    roots = quadratic_solver(2, 4, -5)
    
In this single line of code, the messy details of multiplying, dividing, and square-rooting have all been hidden away from the main program. The details of that calculation have been "encapsulated" in the function.

Any time you import a library into your program--`import java.util.Scanner;` in Java, or `import random` in Python--you are bringing in complicated bits of code that will be available for you to use without having to worry about some of the arcane, or mundane, or complex details that are contained in that code. The concept of encapsulation is extraordinarily powerful.

Programming languages: Machine code, Assembly, High-level
-------------------------------------------------------------

A second way of considering encapsulation is less obvious, but one that we use all the time.

You have almost certainly seen computer programs written in some "high-level" language like Python or Java. These languages are called high-level because they, for the most part, consists of syntax that might be recognized and understood.

Here's a program that's written in C, which adds up the numbers from 0 to 255 and prints out the result:

    # include <stdio.h>

    int main(void)
    {
        int x, sum;
        sum = 0;
        x = 1;
        while (x < 256)
        {
            printf("%d ",x);
            sum = sum + x;
            x = x + 1;
        }
        printf("\nSum = %d\n", sum);
    }

You may not understand everything in this program, but it certainly has a few English words in it, and even someone who doesn't know C very well might be able to work their way through this program to identify how it works.

We have a serious problem, however. You may have heard that computers don't understand English: they only work in *binary digits*, or "bits," the zeroes and ones that are represented by a billion switches being turned "off" or "on."

<i>So how does the computer run this program?</i>

It doesn't. But there is another program on the computer--a *compiler*--that is able to take this program and convert it to something called Assembly Language.

### Assembly Language

I'm going to use the compiler to output a compiled version of the program.

    $ gcc -o sum sum.c</div>

What does this new version of the program look like? We can see the Assembly Language version here:
    
    $ otool -tv sum
    sum:
    (__TEXT,__text) section
    _main:
    0000000100000f10	pushq	%rbp
    0000000100000f11	movq	%rsp, %rbp
    0000000100000f14	subq	$0x20, %rsp
    0000000100000f18	movl	$0x0, -0x4(%rbp)
    0000000100000f1f	movl	$0x0, -0xc(%rbp)
    0000000100000f26	movl	$0x1, -0x8(%rbp)
    0000000100000f2d	cmpl	$0x100, -0x8(%rbp)
    0000000100000f34	jge	0x100000f65
    0000000100000f3a	leaq	0x65(%rip), %rdi
    0000000100000f41	movl	-0x8(%rbp), %esi
    0000000100000f44	movb	$0x0, %al
    0000000100000f46	callq	0x100000f84
    0000000100000f4b	movl	-0xc(%rbp), %esi
    0000000100000f4e	addl	-0x8(%rbp), %esi
    0000000100000f51	movl	%esi, -0xc(%rbp)
    0000000100000f54	movl	-0x8(%rbp), %esi
    0000000100000f57	addl	$0x1, %esi
    0000000100000f5a	movl	%esi, -0x8(%rbp)
    0000000100000f5d	movl	%eax, -0x10(%rbp)
    0000000100000f60	jmp	0x100000f2d
    0000000100000f65	leaq	0x3e(%rip), %rdi
    0000000100000f6c	movl	-0xc(%rbp), %esi
    0000000100000f6f	movb	$0x0, %al
    0000000100000f71	callq	0x100000f84
    0000000100000f76	movl	-0x4(%rbp), %esi
    0000000100000f79	movl	%eax, -0x14(%rbp)
    0000000100000f7c	movl	%esi, %eax
    0000000100000f7e	addq	$0x20, %rsp
    0000000100000f82	popq	%rbp
    0000000100000f83	retq
            
This version of the program contains a series of commands--`push, move, jump, add, call, pop, return`--that manage the data in the program, addresses in memory (listed along the left side), and registers (like `%esi`). Some people program in assembly language, but you can see that it's a much more complicated affair. The process of storing the value `1` in the variable `x` is, in assembly language, `movl	$0x1, -0x8(%rbp)`.

We can say that the assembly language instructions are "encapsulated," or hidden away, so that we don't have to worry about those implementation details. We can write our high-level code, and rest assured that the compilation process will take care of the dirty work for us.

Of course, we still haven't gotten down to the 0s and 1s that the computer needs to run a program. Let's go one step farther down.

      
### Machine Language

In the process of compiling, we actually created a binary version of the program, with nothing but 0s and 1s.

    $ xxd -b sum | cut -c 11-64
    11001111 11111010 11101101 11111110 00000111 00000000
    00000000 00000001 00000011 00000000 00000000 10000000
    00000010 00000000 00000000 00000000 00001111 00000000
    00000000 00000000 10110000 00000100 00000000 00000000
    10000101 00000000 00100000 00000000 00000000 00000000
    00000000 00000000 00011001 00000000 00000000 00000000
    01001000 00000000 00000000 00000000 01011111 01011111
    01010000 01000001 01000111 01000101 01011010 01000101
    01010010 01001111 00000000 00000000 00000000 00000000
    00000000 00000000 00000000 00000000 00000000 00000000
    .
    .
    .
    00100000 00000000 01011111 01011111 01101101 01101000
    01011111 01100101 01111000 01100101 01100011 01110101
    01110100 01100101 01011111 01101000 01100101 01100001
    01100100 01100101 01110010 00000000 01011111 01101101
    01100001 01101001 01101110 00000000 01011111 01110000
    01110010 01101001 01101110 01110100 01100110 00000000
    01100100 01111001 01101100 01100100 01011111 01110011
    01110100 01110101 01100010 01011111 01100010 01101001
    01101110 01100100 01100101 01110010 00000000 00000000
    00000000 00000000


It is *this* code, encapsulated several layers below our original version, that the computer uses to run the program.

These 0s and 1s are used to operate the digital hardware, the memory locations and the logic gates, that produce a given output. In fact, before we had keyboards, mice, and monitors, the personal computer was simply a set of switches with lights above them. Computer code was entered using the individual switches--a long, painful, error-prone process--and output was read from the computer as a series of flashing lights.

Here's a programmer entering a program by hand onto such a machine. The resulting program displays (in binary, of course!) the [prime numbers](https://www.youtube.com/watch?v=wdP8WB8Dwbg) between 2 and 255.

Fortunately, we don't have to enter binary logic instructions by hand. Those codes are encapsulated well beneath our high-level languages.