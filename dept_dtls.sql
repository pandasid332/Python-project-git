select e.empno,e.ename emp_name,e.job,coalesce(e1.ename,'He is the CEO') mgr_name,e.hiredate,e.sal,d.dname,d.loc 
from emp e
join emp e1
on e.mgr=e1.empno(+)
join dept d
on d.deptno=e.deptno;