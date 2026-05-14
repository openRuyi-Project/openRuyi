# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           setools
Version:        4.6.0
Release:        %autorelease
Summary:        Policy analysis tools for SELinux
License:        GPL-2.0-only AND LGPL-2.1-only
URL:            https://github.com/SELinuxProject/setools
#!RemoteAsset:  sha256:d143da7c0f155a67590983c7ff7f7c181c0ebaf350b37a28b34198c6b4b9a5d2
Source0:        https://github.com/SELinuxProject/setools/archive/refs/tags/%{version}.tar.gz
Source1:        setools.pam
Source2:        apol.desktop
BuildSystem:    pyproject

BuildOption(install):  -l setools setoolsgui

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(cython)
BuildRequires:  gcc
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  pkgconfig(libsepol)
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  swig
# For tests.
BuildRequires:  pytest
BuildRequires:  checkpolicy
BuildRequires:  python3dist(networkx) >= 2.6

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
Requires:       python3dist(networkx)

%description    console-analyses
Advanced analysis tools: sedta, seinfoflow.

%package     -n python-setools
Summary:        Policy analysis tools for SELinux
License:        LGPL-2.1-only
Provides:       setools-libs = %{version}-%{release}
Provides:       python3-setools = %{version}-%{release}
%python_provide python3-setools

%description -n python-setools
Python modules for SELinux policy analysis.

%package        gui
Summary:        Policy analysis graphical tools for SELinux
License:        GPL-2.0-only
Requires:       python3-setools = %{version}-%{release}
Requires:       python3-qt6
Requires:       python3dist(networkx)

%description    gui
Graphical tools for SELinux policy analysis (apol).

%generate_buildrequires
%pyproject_buildrequires

%check
# Using %buildroot setools.
rm -rf setools setoolsgui
%pytest tests

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

%files -n python-setools
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
%autochangelog
