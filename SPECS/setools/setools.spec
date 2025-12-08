# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           setools
Version:        4.6.0
Release:        %autorelease
Summary:        Policy analysis tools for SELinux
License:        GPL-2.0-only AND LGPL-2.1-only
URL:            https://github.com/SELinuxProject/setools
#!RemoteAsset
Source0:        https://github.com/SELinuxProject/setools/archive/refs/tags/%{version}.tar.gz
Source1:        setools.pam
Source2:        apol.desktop
BuildSystem:    pyproject

BuildOption(install):  -l setools setoolsgui

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  python3-Cython
BuildRequires:  gcc
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  pkgconfig(libsepol)
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  swig

Requires:       %{name}-console = %{version}-%{release}
Requires:       %{name}-console-analyses = %{version}-%{release}
Requires:       %{name}-gui = %{version}-%{release}

%description
SETools is a collection of graphical tools, command-line tools, and
Python modules designed to facilitate SELinux policy analysis.

%package        console
Summary:        Policy analysis command-line tools for SELinux
License:        GPL-2.0-only
Requires:       python3-setools = %{version}-%{release}
Requires:       libselinux

%description    console
Command-line tools: sediff, seinfo, sesearch.

%package        console-analyses
Summary:        Policy analysis command-line tools for SELinux
License:        GPL-2.0-only
Requires:       python3-setools = %{version}-%{release}
Requires:       libselinux
Requires:       python3-networkx

%description    console-analyses
Advanced analysis tools: sedta, seinfoflow.

%package     -n python3-setools
Summary:        Policy analysis tools for SELinux
License:        LGPL-2.1-only
Provides:       setools-libs = %{version}-%{release}

%description -n python3-setools
Python 3 modules for SELinux policy analysis.

%package        gui
Summary:        Policy analysis graphical tools for SELinux
License:        GPL-2.0-only
Requires:       python3-setools = %{version}-%{release}
Requires:       python3-qt6
Requires:       python3-networkx

%description    gui
Graphical tools for SELinux policy analysis (apol).

%generate_buildrequires
%pyproject_buildrequires

%check

%files console
%license COPYING.GPL
%{_bindir}/sechecker
%{_bindir}/sediff
%{_bindir}/seinfo
%{_bindir}/sesearch
%{_mandir}/man1/sechecker*
%{_mandir}/man1/sediff*
%{_mandir}/man1/seinfo*
%{_mandir}/man1/sesearch*
%{_mandir}/ru/man1/sediff*
%{_mandir}/ru/man1/seinfo*
%{_mandir}/ru/man1/sesearch*

%files console-analyses
%license COPYING.GPL
%{_bindir}/sedta
%{_bindir}/seinfoflow
%{_mandir}/man1/sedta*
%{_mandir}/man1/seinfoflow*
%{_mandir}/ru/man1/sedta*
%{_mandir}/ru/man1/seinfoflow*

%files -n python3-setools
%license COPYING COPYING.LGPL
%{python3_sitearch}/setools/
%{python3_sitearch}/setools-*.dist-info/

%files gui
%license COPYING.GPL
%{_bindir}/apol
%{python3_sitearch}/setoolsgui/
%{_mandir}/man1/apol*
%{_mandir}/ru/man1/apol*

%changelog
%{?autochangelog}
