# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           openvswitch
Version:        3.5.1
Release:        %autorelease
Summary:        Production Quality, Multilayer Open Virtual Switch
License:        Apache-2.0
URL:            https://www.openvswitch.org/
VCS:            git:https://github.com/openvswitch/ovs.git
#!RemoteAsset
Source0:        https://www.openvswitch.org/releases/%{name}-%{version}.tar.gz
Source1:        openvswitch.sysusers
Source2:        ovsdb-server.service
Source3:        ovs-vswitchd.service
Source4:        openvswitch.tmpfiles
BuildSystem:    autotools

BuildOption(conf):  --prefix=%{_prefix}
BuildOption(conf):  --sysconfdir=%{_sysconfdir}
BuildOption(conf):  --localstatedir=%{_localstatedir}
BuildOption(conf):  --with-rundir=/run/openvswitch
BuildOption(conf):  --sbindir=%{_sbindir}
BuildOption(conf):  PYTHON=%{__python3}

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(libcap-ng)
BuildRequires:  pkgconfig(python3)
BuildRequires:  systemd-rpm-macros

%{?systemd_requires}

%description
Open vSwitch provides standard network bridging functions and
support for the OpenFlow protocol for remote per-flow control of
traffic.

%prep -a
# Fix bash completion path
sed -i \
    -e 's|$(sysconfdir)/bash_completion.d|/usr/share/bash-completion/completions|g' \
    -e '/if grep warning:/d' \
    Makefile.am

%conf -p
./boot.sh
export CFLAGS="%{optflags} -ffat-lto-objects"

%install -a
# Install systemd units
install -Dm644 %{SOURCE1} %{buildroot}%{_sysusersdir}/openvswitch.conf
install -Dm644 %{SOURCE2} %{buildroot}%{_unitdir}/ovsdb-server.service
install -Dm644 %{SOURCE3} %{buildroot}%{_unitdir}/ovs-vswitchd.service
install -Dm644 %{SOURCE4} %{buildroot}%{_tmpfilesdir}/openvswitch.conf

# Create config directory
install -dm755 %{buildroot}%{_sysconfdir}/openvswitch

# Remove runtime directory from package
rm -rf %{buildroot}/run

# TODO: make tests pass.
%check

%pre
%sysusers_create_package %{name} %{SOURCE1}

%post
# Initialize the database if it doesn't exist
if [ ! -f %{_sysconfdir}/openvswitch/conf.db ]; then
    echo "Initializing Open vSwitch database..."
    %{_bindir}/ovsdb-tool create \
        %{_sysconfdir}/openvswitch/conf.db \
        %{_datadir}/openvswitch/vswitch.ovsschema
    chown openvswitch:openvswitch %{_sysconfdir}/openvswitch/conf.db
    chmod 0640 %{_sysconfdir}/openvswitch/conf.db
fi

%systemd_post ovsdb-server.service ovs-vswitchd.service

%preun
%systemd_preun ovsdb-server.service ovs-vswitchd.service

%postun
%systemd_postun_with_restart ovsdb-server.service ovs-vswitchd.service

%files
%license LICENSE NOTICE
%doc README.rst NEWS
%dir %{_sysconfdir}/openvswitch
%ghost %config(noreplace) %attr(0640,openvswitch,openvswitch) %{_sysconfdir}/openvswitch/conf.db
%{_bindir}/*
%{_sbindir}/*
%{_libdir}/*.a
%{_libdir}/pkgconfig/*.pc
%{_includedir}/openvswitch/
%{_includedir}/openflow/
%{_datadir}/openvswitch/
%{_datadir}/bash-completion/completions/*.bash
%{_mandir}/man?/*
%{_unitdir}/*.service
%{_sysusersdir}/openvswitch.conf
%{_tmpfilesdir}/openvswitch.conf

%changelog
%{?autochangelog}
