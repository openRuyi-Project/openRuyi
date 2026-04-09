# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           autossh
Version:        1.4g
Release:        %autorelease
Summary:        Automatically restart SSH sessions and tunnels
License:        BSD-3-Clause
URL:            https://www.harding.motd.ca/autossh/
# VCS: No VCS link available
#!RemoteAsset:  sha256:5fc3cee3361ca1615af862364c480593171d0c54ec156de79fc421e31ae21277
Source0:        https://www.harding.motd.ca/autossh/autossh-%{version}.tgz
Source1:        autossh@.service
BuildSystem:    autotools

BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  openssh-clients

Requires:       openssh

%description
Autossh is a program to start a copy of ssh and monitor it, restarting
it as necessary should it die or stop passing traffic.

%prep -a
tar xzf %{SOURCE0} --strip-components=1

# Create a sysusers.d config file
cat >autossh.sysusers.conf <<EOF
u autossh - 'autossh service account' %{_sysconfdir}/autossh -
EOF

%conf -p
autoreconf -fiv

%install -a
install -D -m 444 %{SOURCE1} %{buildroot}/%{_unitdir}/autossh@.service
install -m0644 -D autossh.sysusers.conf %{buildroot}%{_sysusersdir}/autossh.conf

%check
# No tests here.

%post
%systemd_post autossh@.service

%preun
# https://bugzilla.redhat.com/1996234
if [ $1 -eq 0 ] && [ -x /usr/bin/systemctl ]; then
    # Package removal, not upgrade
    if [ -d /run/systemd/system ]; then
        /usr/bin/systemctl --no-reload disable --now autossh@.service || :
	systemctl stop "autossh@*.service" || :
    else
        /usr/bin/systemctl --no-reload disable autossh@.service || :
    fi
fi

%postun
%systemd_postun_with_restart autossh@.service

%files
%doc CHANGES README
%doc autossh.host rscreen
%{_bindir}/autossh
%{_unitdir}/autossh@.service
%{_mandir}/man1/autossh.1*
%{_datadir}/examples/autossh/
%{_sysusersdir}/autossh.conf

%changelog
%autochangelog
