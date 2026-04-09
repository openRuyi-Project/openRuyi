# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           btrbk
Version:        0.32.6
Release:        %autorelease
Summary:        Tool for creating snapshots and remote backups of btrfs sub-volumes
License:        GPL-3.0-or-later
URL:            https://digint.ch/btrbk/
VCS:            https://github.com/digint/btrbk.git
#!RemoteAsset
Source0:        https://digint.ch/download/btrbk/releases/btrbk-%{version}.tar.xz
Source1:        btrbk.logrotate

BuildRequires:  pkgconfig(python3)
BuildRequires:  systemd-rpm-macros
BuildRequires:  make
BuildRequires:  pkgconfig(bash-completion)

Requires:       btrfs-progs
Recommends:     openssh-clients

%description
Backup tool for btrfs sub-volumes, using a configuration file, allows
creation of backups from multiple sources to multiple destinations,
with ssh and flexible retention policy support (hourly, daily,
weekly, monthly)

%prep
%autosetup

%install
make install-bin install-bin-links install-etc install-completion install-systemd install-share \
    DESTDIR=%{buildroot}

%py3_shebang_fix %{buildroot}%{_datadir}/%{name}
install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

%post
%systemd_post %{name}.service
%systemd_post %{name}.timer

%preun
%systemd_preun %{name}.service
%systemd_preun %{name}.timer

%postun
%systemd_postun_with_restart %{name}.service
%systemd_postun_with_restart %{name}.timer

%files
%doc README.md ChangeLog doc/FAQ.md doc/upgrade_to_v0.23.0.md
%license COPYING
%dir %{_sysconfdir}/btrbk
%{_sysconfdir}/btrbk/btrbk.conf.example
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%{_unitdir}/%{name}.*
%{_datadir}/%{name}
%{_bindir}/btrbk
%{_bindir}/lsbtr
%{bash_completions_dir}/btrbk
%{bash_completions_dir}/lsbtr

%changelog
%autochangelog
