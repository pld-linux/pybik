Summary:	A 3D interactive graphics puzzle (similar to a Rubik cube)
Summary(hu.UTF-8):	Pybik egy 3D-s interaktív kirakó (a Rubik-kockához hasonló)
Summary(pl.UTF-8):	Trójwymiarowa interaktywna gra logiczna (podobna do kostki Rubkia)
Name:		pybik
Version:	0.1
Release:	0.1
License:	GPL v3
Group:		X11/Applications/Games
Source0:	http://launchpad.net/pybik/trunk/0.1/+download/%{name}-%{version}.tar.gz
# Source0-md5:	f1c76611fcd393778649d4adacd26217
URL:		https://launchpad.net/pybik
BuildRequires:	python-Pyrex
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	sed >= 4.0
Requires:	python-PyOpenGL
Requires:	python-Pyrex
Requires:	python-modules
Requires:	python-pygtkglext
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pybik is a 3D interactive graphics puzzle (similar to a Rubik cube).

%description -l hu.UTF-8
Pybik egy 3D-s interaktív kirakó (a Rubik-kockához hasonló).

%description -l pl.UTF-8
Pybik to trójwymiarowa interaktywna gra logiczna (podobna do kostki
Rubika).

%prep
%setup -q -n Pybik-%{version}
%{__sed} -i "s@%{_prefix}/local/@%{_prefix}/@g" pybiklib/pybik{,.py}

%build
export CFLAGS="%{rpmcflags}"
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%{__mv} $RPM_BUILD_ROOT%{_datadir}/locale/pt{_PT,}
# req /usr/share/locale/no/LC_MESSAGES not found !!!
%{__rm} -rf $RPM_BUILD_ROOT%{_datadir}/locale/no

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog HACKING NEWS PKG-INFO README THANKS
%attr(755,root,root) %{_bindir}/pybik
%{py_sitedir}/pybiklib/*.py[co]
%{py_sitedir}/pybiklib/drwBlock_c.so
%if "%{py_ver}" > "2.4"
%{py_sitedir}/Pybik-0.1-py2.6.egg-info
%endif
%{_datadir}/pybik
%{_desktopdir}/pybik.desktop
%{_pixmapsdir}/pybik.png
