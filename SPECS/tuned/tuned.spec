# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           tuned
Version:        2.26.0
Release:        %autorelease
Summary:        A dynamic adaptive system tuning daemon
License:        GPL-2.0-or-later
URL:            https://github.com/redhat-performance/tuned
#!RemoteAsset:  sha256:20b6af0752bce2dbcf5406c95077b349dca95d8e5449c8e6a4c05ceddd95ac02
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pyudev)
BuildRequires:  pkgconfig(dbus-python)
BuildRequires:  pkgconfig(systemd)

Requires:       ethtool
Requires:       gawk
Requires:       hdparm
Requires:       polkit
Requires:       util-linux
Requires:       virt-what
Requires:       pkgconfig(dbus-python)
Requires:       python3dist(python-linux-procfs)
Requires:       python3dist(pyudev)
Requires:       python3dist(pyinotify)

%description
The tuned package contains a daemon that tunes system settings dynamically.
It does so by monitoring the usage of several system components periodically.
Based on that information components will then be put into lower or higher
power saving modes to adapt to the current usage. Currently only ethernet
network and ATA harddisk devices are implemented.

%package        gtk
Summary:        GTK+ GUI for tuned
Requires:       %{name} = %{version}-%{release}
Requires:       powertop
Requires:       polkit
Requires:       python3dist(pygobject)

%description    gtk
GTK+ GUI that can control tuned and provides simple profile editor.

%package        ppd
Summary:        PPD compatibility daemon
Requires:       %{name} = %{version}-%{release}

%description    ppd
An API translation daemon that allows applications to easily transition
to TuneD from power-profiles-daemon (PPD).

%package        utils
Requires:       %{name} = %{version}-%{release}
Requires:       powertop
Summary:        Various tuned utilities

%description    utils
This package contains utilities that can help you to fine tune and
debug your system and manage tuned profiles.

%package        utils-systemtap
Summary:        Disk and net statistic monitoring systemtap scripts
Requires:       %{name} = %{version}-%{release}
Requires:       systemtap

%description    utils-systemtap
This package contains several systemtap scripts to allow detailed
manual monitoring of the system. Instead of the typical IO/sec it collects
minimal, maximal and average time between operations to be able to
identify applications that behave power inefficient (many small operations
instead of fewer large ones).

%prep
%autosetup -p1

%build
# Really in fact nothing to build

%install
%make_install DESTDIR="%{buildroot}" BINDIR="%{_bindir}" \
    SBINDIR="%{_sbindir}" DOCDIR="%{_docdir}" PYTHON=%{__python3} \
    TUNED_USER_PROFILES_DIR=%{_sysconfdir}/tuned/profiles \
    TUNED_SYSTEM_PROFILES_DIR=%{_prefix}/lib/tuned/profiles

make install-ppd DESTDIR="%{buildroot}" BINDIR="%{_bindir}" \
    SBINDIR="%{_sbindir}" DOCDIR="%{_docdir}" \
    PYTHON=%{__python3}

# No docs
rm -rf %{buildroot}/%{_datadir}/doc

%post
%systemd_post tuned.service

# migrate all user-defined profiles from /etc/tuned/ to /etc/tuned/profiles/
for f in %{_sysconfdir}/tuned/*; do
    if [ -e "$f/tuned.conf" ]; then
        mv -n "$f" %{_sysconfdir}/tuned/profiles/
    fi
done

%preun
%systemd_preun tuned.service

%postun
%systemd_postun_with_restart tuned.service

%post ppd
%systemd_post tuned-ppd.service

%preun ppd
%systemd_preun tuned-ppd.service

%postun ppd
%systemd_postun_with_restart tuned-ppd.service

%files
%license COPYING
%doc AUTHORS README.md
%{_datadir}/bash-completion/completions/tuned-adm
%{_datadir}/polkit-1/actions/com.redhat.tuned.policy
%{python3_sitelib}/tuned
%{_sbindir}/tuned
%{_sbindir}/tuned-adm
%{_unitdir}/tuned.service
%config %{_sysconfdir}/grub.d
%{_tmpfilesdir}/tuned.conf
%{_sysconfdir}/modprobe.d/tuned.conf
%{_datadir}/dbus-1/system.d/com.redhat.tuned.conf
%dir %{_sysconfdir}/tuned
%config(noreplace) %{_sysconfdir}/tuned/active_profile
%config(noreplace) %{_sysconfdir}/tuned/ppd_base_profile
%config(noreplace) %{_sysconfdir}/tuned/cpu-partitioning-variables.conf
%config(noreplace) %{_sysconfdir}/tuned/cpu-partitioning-powersave-variables.conf
%config(noreplace) %{_sysconfdir}/tuned/tuned-main.conf
%config(noreplace) %{_sysconfdir}/tuned/profile_mode
%config(noreplace) %{_sysconfdir}/tuned/profiles
%config(noreplace) %{_sysconfdir}/tuned/post_loaded_profile
%config(noreplace) %{_sysconfdir}/tuned/realtime-variables.conf
%config(noreplace) %{_sysconfdir}/tuned/realtime-virtual-guest-variables.conf
%config(noreplace) %{_sysconfdir}/tuned/realtime-virtual-host-variables.conf
%config(noreplace) %{_sysconfdir}/tuned/bootcmdline
%{_prefix}/lib/tuned/recommend.d/50-tuned.conf
%dir %{_prefix}/lib/tuned/profiles
%{_prefix}/lib/tuned/profiles/accelerator-performance
%{_prefix}/lib/tuned/profiles/atomic-host
%{_prefix}/lib/tuned/profiles/atomic-guest
%{_prefix}/lib/tuned/profiles/aws
%{_prefix}/lib/tuned/profiles/balanced
%{_prefix}/lib/tuned/profiles/balanced-battery
%{_prefix}/lib/tuned/profiles/cpu-partitioning
%{_prefix}/lib/tuned/profiles/cpu-partitioning-powersave
%{_prefix}/lib/tuned/profiles/default
%{_prefix}/lib/tuned/profiles/desktop
%{_prefix}/lib/tuned/profiles/desktop-powersave
%{_prefix}/lib/tuned/profiles/enterprise-storage
%{_prefix}/lib/tuned/profiles/hpc-compute
%{_prefix}/lib/tuned/profiles/intel-sst
%{_prefix}/lib/tuned/profiles/laptop-ac-powersave
%{_prefix}/lib/tuned/profiles/laptop-battery-powersave
%{_prefix}/lib/tuned/profiles/latency-performance
%{_prefix}/lib/tuned/profiles/mssql
%{_prefix}/lib/tuned/profiles/network-latency
%{_prefix}/lib/tuned/profiles/network-throughput
%{_prefix}/lib/tuned/profiles/openshift
%{_prefix}/lib/tuned/profiles/openshift-control-plane
%{_prefix}/lib/tuned/profiles/openshift-node
%{_prefix}/lib/tuned/profiles/optimize-serial-console
%{_prefix}/lib/tuned/profiles/oracle
%{_prefix}/lib/tuned/profiles/postgresql
%{_prefix}/lib/tuned/profiles/powersave
%{_prefix}/lib/tuned/profiles/realtime
%{_prefix}/lib/tuned/profiles/realtime-virtual-guest
%{_prefix}/lib/tuned/profiles/realtime-virtual-host
%{_prefix}/lib/tuned/profiles/sap-hana
%{_prefix}/lib/tuned/profiles/sap-hana-kvm-guest
%{_prefix}/lib/tuned/profiles/sap-netweaver
%{_prefix}/lib/tuned/profiles/server-powersave
%{_prefix}/lib/tuned/profiles/spectrumscale-ece
%{_prefix}/lib/tuned/profiles/spindown-disk
%{_prefix}/lib/tuned/profiles/throughput-performance
%{_prefix}/lib/tuned/profiles/virtual-guest
%{_prefix}/lib/tuned/profiles/virtual-host
%{_prefix}/lib/tuned/functions
%{_prefix}/lib/kernel/install.d/92-tuned.install
%{_libexecdir}/tuned/defirqaffinity.py
%{_mandir}/man5/tuned*
%{_mandir}/man7/tuned-profiles.7*
%{_mandir}/man7/tuned-profiles-atomic.7*
%{_mandir}/man7/tuned-profiles-compat.7*
%{_mandir}/man7/tuned-profiles-cpu-partitioning.7*
%{_mandir}/man7/tuned-profiles-mssql.7*
%{_mandir}/man7/tuned-profiles-nfv-guest.7*
%{_mandir}/man7/tuned-profiles-nfv-host.7*
%{_mandir}/man7/tuned-profiles-openshift.7*
%{_mandir}/man7/tuned-profiles-oracle.7*
%{_mandir}/man7/tuned-profiles-postgresql.7*
%{_mandir}/man7/tuned-profiles-realtime.7*
%{_mandir}/man7/tuned-profiles-sap-hana.7*
%{_mandir}/man7/tuned-profiles-sap.7*
%{_mandir}/man7/tuned-profiles-spectrumscale-ece.7*
%{_mandir}/man8/tuned*

%files gtk
%{_sbindir}/tuned-gui
%{python3_sitelib}/tuned/gtk
%{_datadir}/tuned/ui
%{_datadir}/icons/hicolor/scalable/apps/tuned.svg
%{_datadir}/applications/tuned-gui.desktop

%files ppd
%{_sbindir}/tuned-ppd
%{_unitdir}/tuned-ppd.service
%{_datadir}/dbus-1/system-services/net.hadess.PowerProfiles.service
%{_datadir}/dbus-1/system.d/net.hadess.PowerProfiles.conf
%{_datadir}/polkit-1/actions/net.hadess.PowerProfiles.policy
%{_datadir}/dbus-1/system-services/org.freedesktop.UPower.PowerProfiles.service
%{_datadir}/dbus-1/system.d/org.freedesktop.UPower.PowerProfiles.conf
%{_datadir}/polkit-1/actions/org.freedesktop.UPower.PowerProfiles.policy
%config(noreplace) %{_sysconfdir}/tuned/ppd.conf

%files utils
%doc COPYING
%{_bindir}/powertop2tuned
%{_libexecdir}/tuned/pmqos-static*

%files utils-systemtap
%doc doc/README.utils
%doc doc/README.scomes
%doc COPYING
%{_sbindir}/varnetload
%{_sbindir}/netdevstat
%{_sbindir}/diskdevstat
%{_sbindir}/scomes
%{_mandir}/man8/varnetload.*
%{_mandir}/man8/netdevstat.*
%{_mandir}/man8/diskdevstat.*
%{_mandir}/man8/scomes.*

%changelog
%autochangelog
