%define	module	faulthandler
#
Summary:	Display the Python traceback on a crash
Name:		python-faulthandler
Version:	2.3
Release:	1
License:	BSD
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/f/faulthandler/faulthandler-%{version}.tar.gz
# Source0-md5:	76d1344adc2302cf5c59a5f8a4f4f4ae
URL:		https://github.com/haypo/faulthandler/wiki
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
Requires:	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fault handler for SIGSEGV, SIGFPE, SIGBUS and SIGILL signals: display
the Python backtrace and restore the previous handler. Allocate an
alternate stack for this handler, if sigaltstack() is available, to be
able to allocate memory on the stack, even on stack overflow.

%prep
%setup  -q -n %{module}-%{version}

%build
%py_build --build-base py2

%install
rm -rf $RPM_BUILD_ROOT

%py_build \
	--build-base py2 \
	install \
	--optimize 2 \
	--root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS PKG-INFO README TODO
%attr(755,root,root) %{py_sitedir}/%{module}.so
%{py_sitedir}/*egg-info
