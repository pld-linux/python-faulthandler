%define	module	faulthandler
Summary:	Display the Python traceback on a crash
Name:		python-faulthandler
Version:	3.0
Release:	1
License:	BSD
Group:		Development/Languages/Python
Source0:	https://github.com/haypo/faulthandler/archive/faulthandler-%{version}.tar.gz
# Source0-md5:	bd628242274c7294c36112bb744a83cf
URL:		http://faulthandler.readthedocs.io/
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fault handler for SIGSEGV, SIGFPE, SIGBUS and SIGILL signals: display
the Python backtrace and restore the previous handler. Allocate an
alternate stack for this handler, if sigaltstack() is available, to be
able to allocate memory on the stack, even on stack overflow.

%prep
%setup -q -n %{module}-%{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README.rst TODO
%attr(755,root,root) %{py_sitedir}/%{module}.so
%{py_sitedir}/*egg-info
%{py_sitedir}/faulthandler.pth
