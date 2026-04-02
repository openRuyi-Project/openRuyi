# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           lxcfs
Version:        6.0.6
Release:        %autorelease
Summary:        FUSE based filesystem for LXC
License:        Apache-2.0
URL:            https://linuxcontainers.org/lxcfs
VCS:            git:https://github.com/lxc/lxcfs
#!RemoteAsset:  sha256:386339ba4cde289b0f6df4fe7a614caa1e45dd91bc0200b4aff6c51bf9d5ef9e
Source:         https://linuxcontainers.org/downloads/lxcfs/lxcfs-%{version}.tar.gz
BuildSystem:    meson

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  python3dist(jinja2)
BuildRequires:  gawk
BuildRequires:  make
BuildRequires:  pkgconfig(fuse3)
BuildRequires:  help2man
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(systemd)

%{?systemd_requires}

%description
LXCFS is a small FUSE filesystem written with the intention of making
Linux containers feel more like a virtual machine. It provides container-aware
procfs files, reflecting the container's own uptime and resource usage.

%install -a
mkdir -p %{buildroot}%{_sharedstatedir}/%{name}

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun %{name}.service

%files
%doc AUTHORS
%license COPYING
%{_bindir}/lxcfs
%dir %{_libdir}/lxcfs
%{_libdir}/lxcfs/liblxcfs.so
%dir %{_datadir}/lxcfs
%{_datadir}/lxcfs/lxc.mount.hook
%{_datadir}/lxcfs/lxc.reboot.hook
%{_mandir}/man1/lxcfs.1*
%{_unitdir}/lxcfs.service
%{_datadir}/lxc/config/common.conf.d/00-lxcfs.conf
%dir %{_sharedstatedir}/lxcfs

%changelog
%{?autochangelog}
