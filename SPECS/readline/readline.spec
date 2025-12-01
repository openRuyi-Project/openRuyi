# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           readline
Version:        8.3
Release:        %autorelease
Summary:        A library for editing typed command lines
License:        GPL-3.0-or-later AND GPL-2.0-or-later AND GFDL-1.3-no-invariants-or-later
URL:            https://tiswww.case.edu/php/chet/readline/rltop.html
#!RemoteAsset
Source0:        https://ftpmirror.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
#!RemoteAsset
Source1:        https://ftpmirror.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz.sig
BuildSystem:    autotools

# Official upstream patches
# Patches are converted to apply with '-p1'
Patch0:         0001-readline-8.3-patch-1.patch

# Other patches
# symbol lookup error: /usr/lib64/libreadline.so.8: undefined symbol: UP
Patch1:         0010-readline-link-ncurses.patch

BuildOption(conf):  --with-curses
BuildOption(conf):  --disable-install-examples

BuildRequires:  make
BuildRequires:  ncurses-devel

%description
The Readline library provides a set of functions that allow users to
edit command lines. Both Emacs and vi editing modes are available. The
Readline library includes additional functions for maintaining a list
of previously-entered command lines for recalling or editing those
lines, and for performing csh-like history expansion on previous
commands.

%package        devel
Summary:        Files needed to develop programs which use the readline library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The Readline library provides a set of functions that allow users to
edit typed command lines. If you want to develop programs that will
use the readline library, you need to have the readline-devel package
installed. You also need to have the readline package installed.

%install -a
# Don't need these
rm -vrf %{buildroot}%{_docdir}/readline
rm -vf %{buildroot}%{_infodir}/dir*

%files
%license COPYING USAGE
%{_libdir}/libreadline.so.*
%{_libdir}/libhistory.so.*
%{_infodir}/history.info*
%{_infodir}/rluserman.info*

%files devel
%doc CHANGES NEWS README
%doc examples/*.c examples/*.h examples/rlfe
%{_includedir}/readline/
%{_libdir}/libreadline.so
%{_libdir}/libhistory.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/pkgconfig/history.pc
%{_mandir}/man3/readline.3*
%{_mandir}/man3/history.3*
%{_infodir}/readline.info*
%{_libdir}/libreadline.a
%{_libdir}/libhistory.a

%changelog
%{?autochangelog}
