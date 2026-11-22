# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Sun Yuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname targetcli

Name:           targetcli
Version:        3.0.2
Release:        %autorelease
Summary:        Command shell for managing the Linux LIO kernel target
License:        Apache-2.0
URL:            https://github.com/open-iscsi/targetcli-fb
#!RemoteAsset:  sha256:00422cce70f1d4a4d804cb1f3f633169ff4ad13b017b7e52d8f49262afe43b9e
Source0:        https://files.pythonhosted.org/packages/source/t/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

# https://github.com/open-iscsi/targetcli-fb/pull/237
Patch2000:      2000-handle-a-missing-system-bus.patch

BuildOption(install):  -l %{srcname}

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(hatch-vcs)
BuildRequires:  python3dist(hatchling)
BuildRequires:  python3dist(packaging)
BuildRequires:  python3dist(pip) >= 19
BuildRequires:  python3dist(configshell-fb)
BuildRequires:  python3dist(pygobject)
BuildRequires:  python3dist(rtslib-fb)

Requires:       python3dist(configshell-fb)
Requires:       python3dist(pygobject)
Requires:       python3dist(rtslib-fb)

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
targetcli is the command shell for the Linux kernel target subsystem (LIO).
It configures backstores, fabrics and access control through configfs, and it
saves and restores the configuration. targetclid keeps the configuration in
sync with the running target.

%generate_buildrequires
%pyproject_buildrequires

%install -a
install -d %{buildroot}%{_sysconfdir}/target %{buildroot}%{_sysconfdir}/target/backup
install -Dm644 targetcli.8 %{buildroot}%{_mandir}/man8/targetcli.8
install -Dm644 targetclid.8 %{buildroot}%{_mandir}/man8/targetclid.8
install -Dm644 systemd/targetclid.service %{buildroot}%{_unitdir}/targetclid.service
install -Dm644 systemd/targetclid.socket %{buildroot}%{_unitdir}/targetclid.socket

%post
%systemd_post targetclid.service targetclid.socket

%preun
%systemd_preun targetclid.service targetclid.socket

%postun
%systemd_postun_with_restart targetclid.service targetclid.socket

%files -f %{pyproject_files}
%dir %{_sysconfdir}/target
%dir %{_sysconfdir}/target/backup
%doc README.md
%{_bindir}/targetcli
%{_bindir}/targetclid
%{_mandir}/man8/targetcli.8*
%{_mandir}/man8/targetclid.8*
%{_unitdir}/targetclid.service
%{_unitdir}/targetclid.socket

%changelog
%autochangelog
