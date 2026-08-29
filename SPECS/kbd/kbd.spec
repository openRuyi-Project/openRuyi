# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%bcond nls 0

Name:           kbd
Version:        2.9.0
Release:        %autorelease
Summary:        Tools for configuring the console (keyboard, virtual terminals, etc.)
License:        GPL-2.0-or-late
URL:            https://kbd-project.org/
VCS:            git:https://git.kernel.org/pub/scm/linux/kernel/git/legion/kbd.git
#!RemoteAsset:  sha256:fb3197f17a99eb44d22a3a1a71f755f9622dd963e66acfdea1a45120951b02ed
Source0:        https://www.kernel.org/pub/linux/utils/%{name}/%{name}-%{version}.tar.xz
Source1:        vlock.pamd
BuildSystem:    autotools

%if %{with nls}
BuildOption(conf):  --enable-nls
%else
BuildOption(conf):  --disable-nls
%endif
BuildOption(conf):  --disable-tests
BuildOption(build):  KEYCODES_PROGS=yes
BuildOption(build):  RESIZECONS_PROGS=yes
BuildOption(install):  KEYCODES_PROGS=yes
BuildOption(install):  RESIZECONS_PROGS=yes

BuildRequires:  bison
BuildRequires:  flex
%if %{with nls}
BuildRequires:  gettext
%endif
BuildRequires:  pkgconfig(pam)
BuildRequires:  make
BuildRequires:  automake

%description
The %{name} package contains tools for managing a Linux
system's console's behavior, including the keyboard, the screen
fonts, the virtual terminals and font files.

%prep -a
aclocal
autoconf -fiv

%install -a
# Install PAM configuration for vlock
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/pam.d
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/pam.d/vlock
%if %{with nls}
%find_lang %{name} --generate-subpackages
%endif

%files
%license COPYING
%doc ChangeLog AUTHORS README docs/doc/font-formats/*.html docs/doc/dvorak/*
%{_bindir}/*
%{_mandir}/*/*
%config(noreplace) %{_sysconfdir}/pam.d/vlock
%{_datadir}/consolefonts/*
%{_datadir}/consoletrans/*
%{_datadir}/unimaps/*
%{_datadir}/keymaps/*

%changelog
%autochangelog
