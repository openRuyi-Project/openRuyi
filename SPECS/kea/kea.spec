# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0
%bcond doc 0

Name:           kea
Version:        3.1.4
Release:        %autorelease
Summary:        DHCPv4, DHCPv6 and DDNS server from ISC
License:        MPL-2.0 AND BSL-1.0
URL:            http://kea.isc.org
VCS:            git:https://gitlab.isc.org/isc-projects/kea.git
#!RemoteAsset:  sha256:a299c976c26b44a51738746fc30584c5ebb174030ef6451aeed0a2d37f9c1dad
Source0:        https://downloads.isc.org/isc/kea/%{version}/kea-%{version}.tar.xz
#!RemoteAsset:  sha256:2478a7259b4eb1899ffc7360bd3c1de4820f543cfebf60087ff95f236adf076b
Source1:        https://downloads.isc.org/isc/kea/%{version}/kea-%{version}.tar.xz.asc
Source2:        kea-dhcp4.service
Source3:        kea-dhcp6.service
Source4:        kea-dhcp-ddns.service
Source5:        kea-ctrl-agent.service
Source6:        kea.sysusers
Source7:        kea.tmpfiles
BuildSystem:    meson

BuildOption(conf):  --install-umask 0022
BuildOption(conf):  -D netconf=disabled
BuildOption(conf):  -D crypto=openssl
BuildOption(conf):  -D krb5=enabled
BuildOption(conf):  -D mysql=enabled
BuildOption(conf):  -D postgresql=disabled

BuildRequires:  boost-devel
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(krb5)
BuildRequires:  pkgconfig(libmariadb)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(valgrind)
BuildRequires:  pkgconfig(log4cplus)
BuildRequires:  pkgconfig(gtest)
BuildRequires:  procps-ng
BuildRequires:  pkgconfig(python3)
BuildRequires:  gcc-c++
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  meson
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
%if %{with doc}
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
%endif

Requires:       coreutils
Requires:       util-linux
%{?systemd_requires}

%description
Kea is an open source software system including DHCPv4, DHCPv6 servers,
Dynamic DNS daemon, REST API interface, MySQL, and PostgreSQL databases,
RADIUS and NETCONF interfaces and related utilities.

%package        devel
Summary:        Development headers and libraries for Kea DHCP server
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       boost-devel
Requires:       pkgconfig(openssl)
Requires:       pkgconfig

%description    devel
Header files and API documentation.

%package        hooks
Summary:        Hooks libraries for kea
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    hooks
Hooking mechanism allow Kea to load one or more dynamically-linked libraries
(known as "hooks libraries") and, at various points in its processing
("hook points"), call functions in them. Those functions perform whatever
custom processing is required.

%build -a
%if %{with doc}
%meson_build doc
%endif

%install -a
rm -f %{buildroot}%{_pkgdocdir}/COPYING

rm -rf %{buildroot}/usr/share/kea/meson-info/

# Create empty password file for the Kea Control Agent
install -m 0640 /dev/null %{buildroot}%{_sysconfdir}/kea/kea-api-password

# Install systemd units
install -Dpm 0644 %{SOURCE2} %{buildroot}%{_unitdir}/kea-dhcp4.service
install -Dpm 0644 %{SOURCE3} %{buildroot}%{_unitdir}/kea-dhcp6.service
install -Dpm 0644 %{SOURCE4} %{buildroot}%{_unitdir}/kea-dhcp-ddns.service
install -Dpm 0644 %{SOURCE5} %{buildroot}%{_unitdir}/kea-ctrl-agent.service

# Start empty lease databases
mkdir -p %{buildroot}%{_sharedstatedir}/kea/
touch %{buildroot}%{_sharedstatedir}/kea/kea-leases4.csv
touch %{buildroot}%{_sharedstatedir}/kea/kea-leases6.csv

# Install systemd sysusers and tmpfiles configs
install -Dpm 0644 %{SOURCE6} %{buildroot}%{_sysusersdir}/kea.conf
install -Dpm 0644 %{SOURCE7} %{buildroot}%{_tmpfilesdir}/kea.conf

mkdir -p %{buildroot}%{_rundir}
install -dm 0750 %{buildroot}%{_rundir}/kea/

mkdir -p %{buildroot}%{_localstatedir}/log
install -dm 0750 %{buildroot}%{_localstatedir}/log/kea/

%pre
%sysusers_create_package %{name} %{SOURCE6}
%tmpfiles_create_package %{name} %{SOURCE7}

%post
# Set a pseudo-random password for default config to secure fresh install and allow CA startup without user intervention
if [[ ! -s %{_sysconfdir}/kea/kea-api-password &&
      -n `grep '"password-file": "kea-api-password"' kea-ctrl-agent.conf` ]]; then
    (umask 0027; head -c 32 /dev/urandom | base64 > kea-api-password)
    chown root:kea kea-api-password
fi
%systemd_post kea-dhcp4.service kea-dhcp6.service kea-dhcp-ddns.service kea-ctrl-agent.service

%preun
%systemd_preun kea-dhcp4.service kea-dhcp6.service kea-dhcp-ddns.service kea-ctrl-agent.service

%postun
%systemd_postun_with_restart kea-dhcp4.service kea-dhcp6.service kea-dhcp-ddns.service kea-ctrl-agent.service

%files
%license COPYING
%doc AUTHORS ChangeLog README CONTRIBUTING.md platforms.rst code_of_conduct.md SECURITY.md
%doc %{_pkgdocdir}/examples
%{_sbindir}/kea*
%{_sbindir}/perfdhcp
%{_libdir}/libkea-*.so.*
%{_unitdir}/kea*.service
%{_datarootdir}/kea
%dir %attr(0750,root,kea) %{_sysconfdir}/kea/
%config(noreplace) %attr(0640,root,kea) %{_sysconfdir}/kea/kea*.conf
%ghost %config(noreplace,missingok) %attr(0640,root,kea) %verify(not md5 size mtime) %{_sysconfdir}/kea/kea-api-password
%dir %attr(0750,kea,kea) %{_sharedstatedir}/kea
%config(noreplace) %attr(0640,kea,kea) %{_sharedstatedir}/kea/kea-leases*.csv
%dir %attr(0750,kea,kea) %{_rundir}/kea/
%dir %attr(0750,kea,kea) %{_localstatedir}/log/kea
%{python3_sitelib}/kea
%{_tmpfilesdir}/kea.conf
%{_sysusersdir}/kea.conf

%files devel
%{_bindir}/kea-msg-compiler
%{_includedir}/kea
%{_libdir}/libkea-*.so
%{_libdir}/pkgconfig/kea.pc

%files hooks
%dir %{_sysconfdir}/kea/radius
%{_sysconfdir}/kea/radius/dictionary
%dir %{_libdir}/kea
%dir %{_libdir}/kea/hooks
%{_libdir}/kea/hooks/lib*.so

%changelog
%autochangelog
