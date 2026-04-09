# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global dialogsubversion 20251001

Name:           dialog
Version:        1.3
Release:        %autorelease
Summary:        A utility for creating TTY dialog boxes
License:        LGPL-2.1-only
URL:            https://invisible-island.net/dialog/dialog.html
VCS:            git:https://github.com/ThomasDickey/dialog-snapshots
#!RemoteAsset
Source:         https://invisible-mirror.net/archives/dialog/dialog-%{version}-%{dialogsubversion}.tgz
BuildSystem:    autotools

BuildOption(build):  CFLAGS="%{optflags}"
BuildOption(build):  LDFLAGS="%{build_ldflags}"

BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  findutils
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  glibc-devel

%description
Dialog is a utility that allows you to show dialog boxes (containing
questions or messages) in TTY (text mode) interfaces.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(ncurses)

%description    devel
This package contains the files needed for developing applications,
which use the dialog library.

# Not standard configure.
# error: unrecognized option: --docdir=/usr/share/doc/dialog
# if we use autoreconf,then it occurs: configure: error: No curses header-files found
%conf
%configure \
    --enable-nls \
    --enable-pc-files \
    --with-libtool \
    --with-ncursesw \
    --includedir=%{_includedir}/dialog

%install -a
rm -rf _samples
mkdir _samples
cp -a samples _samples
rm -rf _samples/samples/install
# Remove execute permission from all files under _samples
find _samples -type f -print0 | xargs -0 chmod a-x

chmod 755 %{buildroot}%{_libdir}/libdialog.so.*.*.*

find %{buildroot} -type f -name "*.a" -delete

# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
%find_lang %{name} --generate-subpackages

%files
%license COPYING
%doc dialog.lsm README _samples/samples
%{_bindir}/dialog
%{_libdir}/libdialog.so.*
%{_mandir}/man1/dialog.*

%files devel
%{_bindir}/dialog-config
%{_includedir}/dialog
%{_libdir}/libdialog.so
%{_libdir}/pkgconfig/dialog.pc
%{_mandir}/man3/dialog.*

%changelog
%autochangelog
