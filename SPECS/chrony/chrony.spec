# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           chrony
Version:        4.8
Release:        %autorelease
Summary:        An NTP client/server
License:        GPL-2.0-only
URL:            https://chrony-project.org
#!RemoteAsset
Source0:        %{url}/releases/chrony-%{version}.tar.gz
#!RemoteAsset
Source1:        %{url}/releases/chrony-%{version}-tar-gz-asc.txt
Source2:        chrony.dhclient
Source3:        chrony.sysusers
Source4:        chronyd.sysconfig
BuildSystem:    autotools

# let systemd create /var/lib/chrony and /var/log/chrony
Patch0:         0001-chrony-nm-dispatcher-dhcp.patch

BuildOption(conf):  --enable-ntp-signd
BuildOption(conf):  --chronyrundir=%{_rundir}/%{name}
BuildOption(conf):  --with-ntp-era=$(date -d '1970-01-01 00:00:00+00:00' +'%s')
BuildOption(conf):  --with-user=chrony
BuildOption(conf):  --with-hwclockfile=%{_sysconfdir}/adjtime
BuildOption(conf):  --with-pidfile=%{_rundir}/%{name}/chronyd.pid
BuildOption(conf):  --with-sendmail=%{_sbindir}/sendmail

BuildRequires:  make
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libedit)
BuildRequires:  pkgconfig(nettle)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(libseccomp)

Requires:       tzdata

Provides:       group(chrony)
Provides:       user(chrony)

%description
chrony is a versatile implementation of the Network Time Protocol (NTP).
It can synchronise the system clock with NTP servers, reference clocks
(e.g. GPS receiver), and manual input using wristwatch and keyboard. It
can also operate as an NTPv4 (RFC 5905) server and peer to provide a time
service to other computers in the network.

%prep -a
# use example chrony.conf as the default config
touch -r examples/chrony.conf.example2 chrony.conf

%install -a
mkdir -p %{buildroot}%{_sysconfdir}/{sysconfig,logrotate.d}
mkdir -p %{buildroot}%{_localstatedir}/{lib,log}/chrony
mkdir -p %{buildroot}%{_sysconfdir}/dhcp/dhclient.d
mkdir -p %{buildroot}%{_libexecdir}
mkdir -p %{buildroot}%{_sysusersdir}
mkdir -p %{buildroot}%{_prefix}/lib/NetworkManager/dispatcher.d
mkdir -p %{buildroot}{%{_unitdir},%{_prefix}/lib/systemd/ntp-units.d}

install -m 644 -p chrony.conf %{buildroot}%{_sysconfdir}/chrony.conf
install -m 755 -p %{SOURCE2} %{buildroot}%{_sysconfdir}/dhcp/dhclient.d/chrony.sh
install -m 644 -p examples/chrony.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/chrony
install -m 644 -p examples/chronyd.service %{buildroot}%{_unitdir}/chronyd.service
install -m 644 -p examples/chronyd-restricted.service %{buildroot}%{_unitdir}/chronyd-restricted.service
install -m 755 -p examples/chrony.nm-dispatcher.onoffline %{buildroot}%{_prefix}/lib/NetworkManager/dispatcher.d/20-chrony-onoffline
install -m 755 -p examples/chrony.nm-dispatcher.dhcp %{buildroot}%{_prefix}/lib/NetworkManager/dispatcher.d/20-chrony-dhcp
install -m 644 -p examples/chrony-wait.service %{buildroot}%{_unitdir}/chrony-wait.service
install -m 644 -p %{SOURCE3} %{buildroot}%{_sysusersdir}/chrony.conf
install -Dpm 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/sysconfig/chronyd

touch %{buildroot}%{_sysconfdir}/chrony.keys
touch %{buildroot}%{_localstatedir}/lib/chrony/{drift,rtc}

echo 'chronyd.service' > %{buildroot}%{_prefix}/lib/systemd/ntp-units.d/50-chronyd.list

%pre
%sysusers_create_package chrony %{SOURCE3}

%post
# migrate from chrony-helper to sourcedir directive
if test -a %{_libexecdir}/chrony-helper; then
        grep -qi 'sourcedir /run/chrony-dhcp$' %{_sysconfdir}/chrony.conf 2> /dev/null || \
                echo -e '\n# Use NTP servers from DHCP.\nsourcedir /run/chrony-dhcp' >> \
                        %{_sysconfdir}/chrony.conf
        mkdir -p /run/chrony-dhcp
        for f in %{_localstatedir}/lib/dhclient/chrony.servers.*; do
                sed 's|.*|server &|' < $f > /run/chrony-dhcp/"${f##*servers.}.sources"
        done 2> /dev/null
fi
%systemd_post chronyd.service chronyd-restricted.service chrony-wait.service

%preun
%systemd_preun chronyd.service chronyd-restricted.service chrony-wait.service

%postun
%systemd_postun_with_restart chronyd.service chronyd-restricted.service

%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc FAQ NEWS README examples/chrony.keys.example
%config(noreplace) %{_sysconfdir}/chrony.conf
%ghost %config %attr(640,root,chrony) %{_sysconfdir}/chrony.keys
%config(noreplace) %{_sysconfdir}/logrotate.d/chrony
%config(noreplace) %{_sysconfdir}/sysconfig/chronyd
%{_sysconfdir}/dhcp/dhclient.d/chrony.sh
%{_bindir}/chronyc
%{_sbindir}/chronyd
%{_prefix}/lib/NetworkManager
%{_prefix}/lib/systemd/ntp-units.d/*.list
%{_unitdir}/chrony*.service
%{_sysusersdir}/chrony.conf
%{_mandir}/man[158]/%{name}*.[158]*
%ghost %dir %attr(750,chrony,chrony) %{_localstatedir}/lib/chrony
%ghost %attr(-,chrony,chrony) %{_localstatedir}/lib/chrony/drift
%ghost %attr(-,chrony,chrony) %{_localstatedir}/lib/chrony/rtc
%ghost %dir %attr(750,chrony,chrony) %{_localstatedir}/log/chrony

%changelog
%autochangelog
