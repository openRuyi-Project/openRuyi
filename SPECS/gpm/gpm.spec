# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define LIBVER 2.1.0

Name:           gpm
Version:        1.20.7
Release:        %autorelease
Summary:        A mouse server for the Linux console
License:        GPL-2.0-or-later
URL:            https://github.com/telmich/gpm
#!RemoteAsset
Source:         https://github.com/telmich/gpm/archive/refs/tags/%{version}.tar.gz
Source1:        gpm.service
BuildSystem:    autotools

Patch0:         0001-some-headers.patch
Patch1:         0002-gpm-1.20.6-multilib.patch
Patch2:         0003-gpm-1.20.1-lib-silent.patch
Patch3:         0004-gpm-1.20.5-close-fds.patch
Patch4:         0005-gpm-1.20.1-weak-wgetch.patch
Patch5:         0006-gpm-1.20.7-rhbz-668480-gpm-types-7-manpage-fixes.patch
Patch6:         0007-src-daemon-remove-obvious-use-of-unitialized-data.patch
Patch7:         0008-src-daemon-reindent-switch-statement-to-avoid-compil.patch
Patch8:         0009-configure-drop-broken-configure-code.patch

BuildOption(build):  CFLAGS="%{optflags} -std=gnu17 -Wno-unused-result -Wno-sign-compare -Wno-pointer-sign"

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  sed
BuildRequires:  gawk
BuildRequires:  texinfo
BuildRequires:  bison
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(libcap-ng)
BuildRequires:  systemd-rpm-macros
BuildRequires:  make
BuildRequires:  gcc

%description
Gpm provides mouse support to text-based Linux applications. It provides
console cut-and-paste operations using the mouse and allows pop-up menus
to appear at the click of a mouse button.

%package        devel
Summary:        Development files for the GPM library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the header files and symbolic links needed to
develop applications that use the GPM library.

%conf -p
./autogen.sh

%install -a
chmod 0755 %{buildroot}/%{_libdir}/libgpm.so.%{LIBVER}
ln -sf libgpm.so.%{LIBVER} %{buildroot}/%{_libdir}/libgpm.so

rm -f %{buildroot}%{_datadir}/emacs/site-lisp/t-mouse.el

mkdir -p %{buildroot}%{_unitdir}
install -m 644 conf/gpm-* %{buildroot}%{_sysconfdir}

# Systemd
mkdir -p %{buildroot}%{_unitdir}
install -m644 %{SOURCE1} %{buildroot}%{_unitdir}

find %{buildroot} -type f -name "*.a" -delete -print

%post
%systemd_post gpm.service

%preun
%systemd_preun gpm.service

%postun
%systemd_postun_with_restart gpm.service

%files
%doc COPYING README TODO
%doc doc/README* doc/FAQ doc/Announce doc/changelog
%{_infodir}/gpm.info*
%config(noreplace) %{_sysconfdir}/gpm-*
%{_unitdir}/gpm.service
%{_bindir}/*
%if "%{_sbindir}" != "%{_bindir}"
%{_sbindir}/*
%endif
%{_mandir}/man?/*
%{_libdir}/libgpm.so.*

%files devel
%{_includedir}/*
%{_libdir}/libgpm.so

%changelog
%autochangelog
