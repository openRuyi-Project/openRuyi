# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global upstreamversion 2024-07

Name:           picocom
Version:        2024.07
Release:        %autorelease
Summary:        Minimal dumb-terminal emulation program
License:        GPL-2.0-or-later
URL:            https://gitlab.com/wsakernel/picocom
#!RemoteAsset
Source0:        https://gitlab.com/wsakernel/picocom/-/archive/%{upstreamversion}/picocom-%{upstreamversion}.tar.bz2
Source1:        picocom.sysusers
BuildSystem:    autotools

BuildOption(build):  CC="%{__cc}"
BuildOption(build):  CFLAGS="%{build_cflags} -DUSE_CUSTOM_BAUD"
BuildOption(build):  UUCP_LOCK_DIR=/run/lock/picocom

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  systemd-rpm-macros

Requires(pre):  systemd-sysusers

%description
picocom is a minimal dumb-terminal emulation program. It is very much like
minicom, but smaller and simpler. It is ideal for embedded systems.

# No configure.
%conf

# No install.
%install
install -D -p -m 755 picocom %{buildroot}%{_bindir}/picocom
install -d -m 0775 %{buildroot}/run/lock/picocom
install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/picocom.conf

# No tests.
%check

%pre
%sysusers_create_package picocom %{SOURCE3}

%files
%license LICENSE.txt
%doc CONTRIBUTORS README.md
%dir %attr(0775,root,dialout) /run/lock/picocom
%{_bindir}/picocom
%{_sysusersdir}/picocom.conf

%changelog
%autochangelog
