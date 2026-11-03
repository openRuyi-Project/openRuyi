# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           lxc
Version:        7.0.0
Release:        %autorelease
Summary:        Linux Resource Containers
License:        LGPL-2.1-or-later AND GPL-2.0-only
URL:            https://linuxcontainers.org/lxc
VCS:            git:https://github.com/lxc/lxc
#!RemoteAsset:  sha256:ba0c860626efbac6683f351dd718edb062065e919716d787b89e3d547c5d9493
Source0:        https://linuxcontainers.org/downloads/lxc/lxc-%{version}.tar.gz
Source1:        lxc-net
BuildSystem:    meson

BuildOption(conf):  -D examples=true
BuildOption(conf):  -D man=true
BuildOption(conf):  -D tools=true
BuildOption(conf):  -D commands=true
BuildOption(conf):  -D capabilities=true
BuildOption(conf):  -D openssl=true
BuildOption(conf):  -D selinux=true
BuildOption(conf):  -D seccomp=true
BuildOption(conf):  -D memfd-rexec=true
BuildOption(conf):  -D thread-safety=true
BuildOption(conf):  -D dbus=true
BuildOption(conf):  -D tests=false
BuildOption(conf):  -D init-script=systemd
BuildOption(conf):  -D systemd-unitdir=%{_unitdir}
BuildOption(conf):  -D distrosysconfdir=sysconfig
BuildOption(conf):  -D pam-cgroup=true
BuildOption(conf):  -D runtime-path=%{_rundir}
BuildOption(conf):  -D man=false

BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  gcc-c++
BuildRequires:  glibc
BuildRequires:  util-linux
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(pam)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(libseccomp)

Requires:       lxcfs
Requires:       rsync
Requires:       openssl
Requires:       wget
%{?systemd_requires}

%patchlist
# https://github.com/lxc/lxc/commit/06f626091cb9f1d717cb9d63b7bc2ffdbf0c3cdf
1000-commands-validate-string-in-lxc_cmd_get_config_item_callback.patch
# https://github.com/lxc/lxc/commit/19ad80ed8e6288904caaee5b7bd3c485d51a2291
1001-commands-validate-datalen-in-lxc_cmd_console_log_callback.patch
# https://github.com/lxc/lxc/commit/6424a91a55efc54edc25ca46e9165bd9f35b50b7
1002-lxc-copy-open-hostname-in-a-safer-way.patch
# https://github.com/lxc/lxc/commit/fa12709a79c2b63b3918297d7505108fcc840eb6
1003-lxc-copy-fix-hostname-truncation-during-clone.patch

%description
Linux Resource Containers provide process and resource isolation without the
overhead of full virtualization. This package contains the main command-line tools.

%package        devel
Summary:        Development files for lxc
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains libraries and header files for developing applications
that use LXC.

%install -a
mkdir -p %{buildroot}%{_sharedstatedir}/lxc
mkdir -p %{buildroot}%{_localstatedir}/cache/lxc
rm -f %{buildroot}%{_libdir}/liblxc.a
install -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/sysconfig/lxc-net

%post
%systemd_post lxc-net.service lxc.service lxc-monitord.service

%preun
%systemd_preun lxc-net.service lxc.service lxc-monitord.service

%postun
%systemd_postun lxc-net.service lxc.service lxc-monitord.service

%files
%doc AUTHORS README.md
%license COPYING
%{_bindir}/lxc-*
%{_datadir}/bash-completion/completions/*
%{_datadir}/lxc/*
%{_datadir}/doc/lxc/examples/*
%{_libdir}/liblxc.so.*
%{_libdir}/lxc
%{_libexecdir}/lxc
%{_sbindir}/init.lxc
%{_sharedstatedir}/lxc
%dir %{_sysconfdir}/lxc
%config(noreplace) %{_sysconfdir}/lxc/default.conf
%config(noreplace) %{_sysconfdir}/sysconfig/lxc
%config(noreplace) %{_sysconfdir}/sysconfig/lxc-net
%{_unitdir}/lxc.service
%{_unitdir}/lxc@.service
%{_unitdir}/lxc-net.service
%{_unitdir}/lxc-monitord.service
%dir %{_localstatedir}/cache/lxc
%{_libdir}/security/pam_cgfs.so

%files devel
%{_libdir}/pkgconfig/lxc.pc
%{_includedir}/lxc
%{_libdir}/liblxc.so

%changelog
%autochangelog
