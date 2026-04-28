# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           nvme-cli
Version:        2.16
Release:        %autorelease
Summary:        NVMe management command line interface
License:        GPL-2.0-only
URL:            https://github.com/linux-nvme/nvme-cli
#!RemoteAsset:  sha256:989682ed7b250a2c7a8127e362ffc5d29f5c370127abe405be09c73216da2b97
Source0:        https://github.com/linux-nvme/nvme-cli/archive/v%{version}.tar.gz
BuildSystem:    meson

BuildOption(conf):  -Dudevrulesdir=%{_udevrulesdir}
BuildOption(conf):  -Dsystemddir=%{_unitdir}
BuildOption(conf):  -Ddocs=man

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  meson
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(json-c) >= 0.13
BuildRequires:  pkgconfig(libnvme) >= 1.15
BuildRequires:  pkgconfig(libnvme-mi)
BuildRequires:  pkgconfig(libudev)
%{?systemd_requires}

%description
nvme-cli provides NVM-Express user space tooling for Linux.

%install -a
# hostid and hostnqn are supposed to be unique per machine. We obviously
# can't package them.
rm -f %{buildroot}%{_sysconfdir}/nvme/hostid
rm -f %{buildroot}%{_sysconfdir}/nvme/hostnqn

# Do not install the dracut rule yet. See rhbz 1742764
rm -f %{buildroot}/usr/lib/dracut/dracut.conf.d/70-nvmf-autoconnect.conf

%post
%systemd_post nvmefc-boot-connections.service
%systemd_post nvmf-autoconnect.service
%systemd_post nvmf-connect@.service
%systemd_post nvmf-connect-nbft.service
if [ -S /run/udev/control ]; then
    udevadm control --reload
    udevadm trigger
fi

%preun
%systemd_preun nvmefc-boot-connections.service
%systemd_preun nvmf-autoconnect.service
%systemd_preun nvmf-connect@.service
%systemd_preun nvmf-connect-nbft.service

%postun
%systemd_postun nvmefc-boot-connections.service
%systemd_postun nvmf-autoconnect.service
%systemd_postun nvmf-connect@.service
%systemd_postun nvmf-connect-nbft.service

%files
%license LICENSE
%doc README.md
%{_sbindir}/nvme
%{_datadir}/bash-completion/completions/nvme
%{_datadir}/zsh/site-functions/_nvme
%dir %{_sysconfdir}/nvme
%{_sysconfdir}/nvme/discovery.conf
%{_unitdir}/nvmefc-boot-connections.service
%{_unitdir}/nvmf-autoconnect.service
%{_unitdir}/nvmf-connect.target
%{_unitdir}/nvmf-connect@.service
%{_unitdir}/nvmf-connect-nbft.service
%{_udevrulesdir}/71-nvmf-hpe.rules
%{_udevrulesdir}/70-nvmf-autoconnect.rules
%{_udevrulesdir}/70-nvmf-keys.rules
%{_udevrulesdir}/71-nvmf-netapp.rules
%{_udevrulesdir}/71-nvmf-vastdata.rules
%{_udevrulesdir}/65-persistent-net-nbft.rules
%{_mandir}/man1/nvme*

%changelog
%autochangelog
