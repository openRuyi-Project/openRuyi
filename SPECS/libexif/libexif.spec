# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: panglars <panghao.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libexif
Version:        0.6.26
Release:        %autorelease
Summary:        Library for parsing, editing, and saving EXIF data
License:        LGPL-2.0-or-later
URL:            https://libexif.github.io/
VCS:            git:https://github.com/libexif/libexif.git
#!RemoteAsset:  sha256:4a055ed6575e61ca46c3172be3c753cc16c9becd0f99ec71d58dd0e471476c0c
Source0:        https://github.com/libexif/libexif/releases/download/v%{version}/%{name}-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --disable-docs
BuildOption(conf):  --disable-static

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  diffutils
BuildRequires:  gettext-devel
BuildRequires:  libtool
BuildRequires:  make

%description
libexif is a library for parsing, editing, and saving EXIF data. It is
intended to replace redundant EXIF implementations in command-line utilities
and graphical applications.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains the libraries and header files needed for
developing applications that use %{name}.

%conf -p
autoreconf -fiv

%check
%make_build check

%install -a
rm -f %{buildroot}%{_libdir}/*.a
%find_lang libexif-12 --all-name --generate-subpackages

%files -f %{name}-english.lang
%doc %{_docdir}/libexif/ABOUT-NLS
%doc %{_docdir}/libexif/AUTHORS
%doc %{_docdir}/libexif/ChangeLog
%doc %{_docdir}/libexif/NEWS
%doc %{_docdir}/libexif/README
%doc %{_docdir}/libexif/SECURITY.md
%license %{_docdir}/libexif/COPYING
%{_libdir}/libexif.so.*

%files devel
%{_includedir}/libexif/
%{_libdir}/libexif.so
%{_libdir}/pkgconfig/libexif.pc

%changelog
%autochangelog
