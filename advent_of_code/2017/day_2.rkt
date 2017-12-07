#lang racket
(define (part1)
  (process-input)
  )

(define (process-row-aux xs)
  (if (null? (cdr xs))
      (cons (car xs) (car xs))
      ;;(process-row-aux (max maxx (car xs)) (min minn (car xs)) (cdr xs))
      )
  )

(define (process-row row)
  (let ([minmax (process-row-aux (car row) (car row) row)])
    (- (max (car minmax) (cdr minmax)) (min (cdr minmax) (car minmax)))
    )
  )

(define (process-input)
  (let ([input (read-line)])
    (if (equal? input eof)
        0
        (+ (process-row (map string->number (string-split input))) (process-input))
        )
    )
  )

;;

(define (part2)
  (process-input2)
  )



;;(part1)
(part2)