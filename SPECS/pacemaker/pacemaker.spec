# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global archive_version Pacemaker-3.0.1

Name:           pacemaker
Version:        3.0.1
Release:        %autorelease
Summary:        Scalable High-Availability cluster resource manager
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://www.clusterlabs.org/pacemaker/
VCS:            git:https://github.com/ClusterLabs/pacemaker.git
#!RemoteAsset:  sha256:17a823c52d5448de817162f334b038598e22ea3e24e63a8819f978fac2b252e4
Source0:        https://github.com/ClusterLabs/%{name}/archive/refs/tags/%{archive_version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        pacemaker.sysusers
BuildSystem:    autotools

BuildOption(prep):  -n %{name}-%{archive_version}
BuildOption(conf):  --disable-hardening
BuildOption(conf):  --disable-static
BuildOption(conf):  --enable-fatal-warnings=no
BuildOption(conf):  --localstatedir=%{_var}
BuildOption(conf):  --with-corosync
BuildOption(conf):  --with-initdir=%{_initrddir}
BuildOption(conf):  --with-runstatedir=%{_rundir}
BuildOption(conf):  --with-systemdsystemunitdir=%{_unitdir}
BuildOption(conf):  --with-version=%{version}-%{release}
BuildOption(conf):  PYTHON=%{__python3}

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  corosync-devel
BuildRequires:  docbook-xsl
BuildRequires:  gettext-devel
BuildRequires:  help2man
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(libqb)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(pam)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  resource-agents
BuildRequires:  systemd-rpm-macros

Requires:       corosync%{?_isa} >= 2.0.0
Requires:       resource-agents

Provides:       group(haclient)
Provides:       user(hacluster)

%description
Pacemaker is an advanced, scalable high-availability cluster resource
manager. It makes use of messaging and membership services provided by
Corosync to detect, communicate about, and recover from node and
resource-level failures.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       corosync-devel
Requires:       pkgconfig
Requires:       pkgconfig(glib-2.0)
Requires:       pkgconfig(libqb)
Requires:       pkgconfig(libxml-2.0)
Requires:       pkgconfig(libxslt)
Requires:       pkgconfig(uuid)

%description    devel
This package contains the header files, shared library symlinks and
pkg-config files needed to develop applications that link against the
Pacemaker libraries.

%package        doc
Summary:        Documentation for %{name}
License:        CC-BY-SA-4.0
BuildArch:      noarch

%description    doc
This package contains documentation for Pacemaker.

%conf -p
./autogen.sh
# Upstream Makefile only links -lncurses; cbreak() lives in libtinfo and
# the linker no longer follows DT_NEEDED of indirect deps by default,
# so pull libtinfo via --copy-dt-needed-entries. Keep %{build_ldflags}
# so distro hardening flags stay in effect.
export LDFLAGS="%{build_ldflags} -Wl,--copy-dt-needed-entries"

%install -a
install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/pacemaker.conf
mkdir -p %{buildroot}%{_localstatedir}/lib/rpm-state/%{name}
# Drop fence_legacy, deprecated and unused.
rm -f %{buildroot}%{_sbindir}/fence_legacy
rm -f %{buildroot}%{_mandir}/man8/fence_legacy.*
# Drop the CTS (Cluster Test Suite); openRuyi does not ship a
# pacemaker-cts subpackage and downstream consumers (ceph) do not
# need it. The runtime python helpers (_library, exitstatus,
# buildoptions) used by tools like pcmk_simtimes are kept.
rm -rf %{buildroot}%{python3_sitelib}/pacemaker/_cts
rm -f  %{buildroot}%{_libexecdir}/pacemaker/cts-support
rm -rf %{buildroot}%{_datadir}/pacemaker/tests

%check
# Upstream tests need a privileged runtime environment (live cluster
# IPC, systemd, network) that is not available inside the build chroot.

%pre
%sysusers_create_package %{name} %{SOURCE1}

%post
%systemd_post pacemaker.service pacemaker_remote.service crm_mon.service

%preun
%systemd_preun pacemaker.service pacemaker_remote.service crm_mon.service

%postun
%systemd_postun_with_restart pacemaker.service crm_mon.service

%files
%doc COPYING ChangeLog.md
%license licenses/GPLv2 licenses/LGPLv2.1
%{_sysusersdir}/pacemaker.conf
%dir %attr(750, root, haclient) %{_sysconfdir}/pacemaker
%config(noreplace) %{_sysconfdir}/sysconfig/pacemaker
%config(noreplace) %{_sysconfdir}/sysconfig/crm_mon
%config(noreplace) %{_sysconfdir}/logrotate.d/pacemaker
%{_sbindir}/attrd_updater
%{_sbindir}/cibadmin
%{_sbindir}/crm_attribute
%{_sbindir}/crm_diff
%{_sbindir}/crm_error
%{_sbindir}/crm_failcount
%{_sbindir}/crm_master
%{_sbindir}/crm_mon
%{_sbindir}/crm_node
%{_sbindir}/crm_report
%{_sbindir}/crm_resource
%{_sbindir}/crm_rule
%{_sbindir}/crm_shadow
%{_sbindir}/crm_simulate
%{_sbindir}/crm_standby
%{_sbindir}/crm_ticket
%{_sbindir}/crm_verify
%{_sbindir}/crmadmin
%{_sbindir}/fence_watchdog
%{_sbindir}/iso8601
%{_sbindir}/pacemakerd
%{_sbindir}/pacemaker-remoted
%{_sbindir}/stonith_admin
%{_libexecdir}/pacemaker/
%{_unitdir}/pacemaker.service
%{_unitdir}/pacemaker_remote.service
%{_unitdir}/crm_mon.service
%{_libdir}/libcib.so.*
%{_libdir}/libcrmcluster.so.*
%{_libdir}/libcrmcommon.so.*
%{_libdir}/libcrmservice.so.*
%{_libdir}/liblrmd.so.*
%{_libdir}/libpacemaker.so.*
%{_libdir}/libpe_rules.so.*
%{_libdir}/libpe_status.so.*
%{_libdir}/libstonithd.so.*
# Runtime python helpers used by pacemaker tools (e.g. pcmk_simtimes);
# the _cts test suite is excluded above in %install.
%{python3_sitelib}/pacemaker/
%dir %{_prefix}/lib/ocf
%dir %{_prefix}/lib/ocf/resource.d
%{_prefix}/lib/ocf/resource.d/pacemaker
%dir %{_datadir}/pacemaker
%{_datadir}/pacemaker/*.rng
%{_datadir}/pacemaker/*.xsl
%{_datadir}/pacemaker/api
%{_datadir}/pacemaker/base
%{_datadir}/pacemaker/alerts
%{_datadir}/pacemaker/report.collector
%{_datadir}/pacemaker/report.common
%{_datadir}/pkgconfig/pacemaker-schemas.pc
%{_datadir}/snmp/mibs/PCMK-MIB.txt
%dir %attr(750, hacluster, haclient) %{_var}/lib/pacemaker
%dir %attr(750, hacluster, haclient) %{_var}/lib/pacemaker/blackbox
%dir %attr(750, hacluster, haclient) %{_var}/lib/pacemaker/cib
%dir %attr(750, hacluster, haclient) %{_var}/lib/pacemaker/cores
%dir %attr(750, hacluster, haclient) %{_var}/lib/pacemaker/pengine
%dir %attr(770, hacluster, haclient) %{_var}/log/pacemaker
%dir %attr(770, hacluster, haclient) %{_var}/log/pacemaker/bundles
%ghost %dir %{_localstatedir}/lib/rpm-state/%{name}
%{_mandir}/man7/*pacemaker*.7*
%{_mandir}/man8/attrd_updater.8*
%{_mandir}/man8/cibadmin.8*
%{_mandir}/man8/crm*.8*
%{_mandir}/man8/fence_watchdog.8*
%{_mandir}/man8/iso8601.8*
%{_mandir}/man8/pacemakerd.8*
%{_mandir}/man8/pacemaker-remoted.8*
%{_mandir}/man8/stonith_admin.8*

%files devel
%{_includedir}/pacemaker/
%{_libdir}/libcib.so
%{_libdir}/libcrmcluster.so
%{_libdir}/libcrmcommon.so
%{_libdir}/libcrmservice.so
%{_libdir}/liblrmd.so
%{_libdir}/libpacemaker.so
%{_libdir}/libpe_rules.so
%{_libdir}/libpe_status.so
%{_libdir}/libstonithd.so
%{_libdir}/pkgconfig/libpacemaker.pc
%{_libdir}/pkgconfig/pacemaker.pc
%{_libdir}/pkgconfig/pacemaker-cib.pc
%{_libdir}/pkgconfig/pacemaker-cluster.pc
%{_libdir}/pkgconfig/pacemaker-fencing.pc
%{_libdir}/pkgconfig/pacemaker-lrmd.pc
%{_libdir}/pkgconfig/pacemaker-pe_rules.pc
%{_libdir}/pkgconfig/pacemaker-pe_status.pc
%{_libdir}/pkgconfig/pacemaker-service.pc

%files doc
%license licenses/CC-BY-SA-4.0
%doc %{_docdir}/%{name}/

%changelog
%autochangelog
