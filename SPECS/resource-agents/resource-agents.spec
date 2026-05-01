# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           resource-agents
Version:        4.18.0
Release:        %autorelease
Summary:        Open Source HA reusable cluster resource scripts
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://github.com/ClusterLabs/resource-agents
#!RemoteAsset:  sha256:2570e473a8693ae36f130aa3edfddba0300b12c8897aaa4ce0af87aa2afca9d4
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-libnet
BuildOption(conf):  --enable-fatal-warnings=no
BuildOption(conf):  --with-pkg-name=%{name}
BuildOption(conf):  --with-ras-set=linux-ha
BuildOption(conf):  --with-rsctmpdir=/run/%{name}

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  docbook-dtds
BuildRequires:  docbook-xsl
BuildRequires:  libtool
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  perl(Pod::Man)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libqb)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  which

%description
A set of scripts to interface with several services to operate in a
High Availability environment for both Pacemaker and rgmanager service
managers. This package contains the linux-ha (Open Cluster Framework)
resource agents.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
This package contains the header files and pkg-config files needed for
developing applications that depend on %{name}.

%package        ldirectord
Summary:        A monitoring daemon for maintaining high availability resources
License:        GPL-2.0-or-later
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ipvsadm
Requires:       logrotate
Requires:       perl(LWP)
Requires:       perl(Mail::Send)
Requires:       perl(Net::SSLeay)

%description    ldirectord
ldirectord is a daemon that monitors real servers in an LVS-based load
balancer and adjusts the kernel IPVS rules to route traffic only to
healthy servers.

%conf -p
autoreconf -fiv

%install -a
# remove duped documents
rm -rf %{buildroot}%{_docdir}/%{name}

%check
# Upstream does not ship an automated test suite that can run in the
# build chroot.

%post ldirectord
%systemd_post ldirectord.service

%preun ldirectord
%systemd_preun ldirectord.service

%postun ldirectord
%systemd_postun_with_restart ldirectord.service

%files
%doc AUTHORS ChangeLog
%license COPYING COPYING.GPLv3 COPYING.LGPL
%dir %{_prefix}/lib/ocf
%dir %{_prefix}/lib/ocf/resource.d
%dir %{_prefix}/lib/ocf/lib
%{_prefix}/lib/ocf/lib/heartbeat
%{_prefix}/lib/ocf/resource.d/heartbeat
%exclude %{_prefix}/lib/ocf/resource.d/heartbeat/ldirectord
%{_unitdir}/resource-agents-deps.target
%{_tmpfilesdir}/%{name}.conf
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/ocft
%{_datadir}/%{name}/ocft/configs
%{_datadir}/%{name}/ocft/caselib
%{_datadir}/%{name}/ocft/README
%{_datadir}/%{name}/ocft/README.zh_CN
%{_datadir}/%{name}/ocft/helpers.sh
%exclude %{_datadir}/%{name}/ocft/runocft
%exclude %{_datadir}/%{name}/ocft/runocft.prereq
%{_sbindir}/ocf-tester
%{_sbindir}/ocft
%{_mandir}/man7/*.7*
%{_mandir}/man8/ocf-tester.8*
%dir %{_sysconfdir}/ha.d
%{_sysconfdir}/ha.d/shellfuncs
%{_libexecdir}/heartbeat

%files devel
%{_datadir}/%{name}/ra-api-1.dtd
%{_datadir}/%{name}/metadata.rng
%{_includedir}/heartbeat
%{_datadir}/pkgconfig/%{name}.pc

%files ldirectord
%{_sbindir}/ldirectord
%doc ldirectord/ldirectord.cf
%{_mandir}/man8/ldirectord.8*
%config(noreplace) %{_sysconfdir}/logrotate.d/ldirectord
%dir %{_sysconfdir}/ha.d/resource.d
%{_sysconfdir}/ha.d/resource.d/ldirectord
%{_unitdir}/ldirectord.service
%exclude %{_sysconfdir}/init.d/ldirectord
%{_prefix}/lib/ocf/resource.d/heartbeat/ldirectord

%changelog
%autochangelog
