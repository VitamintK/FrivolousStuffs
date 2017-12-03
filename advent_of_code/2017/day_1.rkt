#lang racket
;;run by doing "C:\Program Files\Racket\Racket.exe" day_1.rkt < day_1.in
;;(require racket/port)
(define (count-adj xs prev)
  (if (null? xs)
       0
      (if (equal? (car xs) prev)
          (+ (- (char->integer (car xs)) 48) (count-adj (cdr xs) (car xs)))
          (count-adj (cdr xs) (car xs)))
   )
 )
(define (get-last xs)
  (if (null? (cdr xs))
      (car xs)
      (get-last (cdr xs))
      )
  )




;;part 2
(define (get-halfway slow fast)
  (if (null? fast)
      slow
      (get-halfway (cdr slow) (cdr (cdr fast)))
      )
  )

(define (count-opp start mid)
  (if (null? mid)
      0
      (if (equal? (car start) (car mid))
          (+ (- (char->integer (car start)) 48) (count-opp (cdr start) (cdr mid)))
          (count-opp (cdr start) (cdr mid))
          )
      )
  )


;;part 1
;;(let ([input (string->list (port->string))])
;;  (count-adj (cons (get-last input) input) null)
;;  )

;;part 2
(let ([input (string->list (port->string))])
  (* 2 (count-opp input (get-halfway input input)))
  )