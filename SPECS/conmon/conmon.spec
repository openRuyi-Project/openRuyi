# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: corestudy <2760018909@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           conmon
Version:        2.2.1
Release:        %autorelease
Summary:        OCI container runtime monitor
License:        Apache-2.0
URL:            https://github.com/containers/conmon
#!RemoteAsset:  sha256:814fb5979a3a4b8576b1f901e606b482bebb41cb7e57926e6d5765ee786b96d3
Source0:        https://github.com/containers/conmon/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    autotools

BuildOption(build):  DEBUGFLAG="-g"
BuildOption(build):  bin/conmon
BuildOption(install):  PREFIX=%{_prefix}
BuildOption(install):  install.bin

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libseccomp)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  go-md2man

Requires:       glib

%description
Conmon is a monitoring program for OCI container runtimes. It is used by
Podman and CRI-O to monitor the container process, holding open the tty
and handling logging.

%prep -a
sed -i 's/install.bin: bin\/conmon/install.bin:/' Makefile

# No configure.
%conf

%build -a
make GOMD2MAN=go-md2man -C docs

%install -a
make PREFIX=%{buildroot}%{_prefix} -C docs install

%check
# skip tests as the env is not support.

%files
%license LICENSE
%doc README.md
%{_bindir}/conmon
%{_mandir}/man8/conmon.8*

%changelog
%autochangelog
