# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           ebook-tools
Version:        0.2.2
Release:        %autorelease
Summary:        Tools for accessing and converting various ebook file formats
License:        MIT
URL:            http://sourceforge.net/projects/ebook-tools/
VCS:            svn:https://svn.code.sf.net/p/ebook-tools
#!RemoteAsset:  sha256:cbc35996e911144fa62925366ad6a6212d6af2588f1e39075954973bbee627ae
Source0:        http://downloads.sourceforge.net/ebook-tools/%{name}-%{version}.tar.gz
BuildSystem:    cmake

BuildOption(conf):  -DCMAKE_POLICY_VERSION_MINIMUM=3.5

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libzip)
BuildRequires:  make

%description
Tools for accessing and converting various ebook file formats.
This package contains the command line tools.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%files
%doc README
%license LICENSE
%{_bindir}/einfo
%{_bindir}/lit2epub
%{_libdir}/libepub.so.*

%files	devel
%{_libdir}/libepub.so
%{_includedir}/epub*.h

%changelog
%autochangelog
