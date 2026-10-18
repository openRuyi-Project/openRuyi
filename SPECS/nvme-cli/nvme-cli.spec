# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           nvme-cli
Version:        3.1
Release:        %autorelease
Summary:        NVMe management command line interface
License:        GPL-2.0-only AND LGPL-2.1-or-later
URL:            https://github.com/linux-nvme/nvme-cli
#!RemoteAsset:  sha256:8a6879f1f2af53743c03a8f77f247261306300d3f3b0edfd242c5f646bdfdccb
Source0:        https://github.com/linux-nvme/nvme-cli/archive/v%{version}.tar.gz
BuildSystem:    meson

BuildOption(conf):  -Dudevrulesdir=%{_udevrulesdir}
BuildOption(conf):  -Dsystemddir=%{_unitdir}
BuildOption(conf):  -Ddocs=man
BuildOption(conf):  -Dpython=disabled

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  meson
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(json-c) >= 0.13
BuildRequires:  pkgconfig(libkeyutils)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(openssl)
%{?systemd_requires}
Provides:       %{name}-libs = %{version}-%{release}

%description
nvme-cli provides NVM-Express user space tooling for Linux.
It also ships libnvme3, the NVMe device management library bundled since 3.0.

%package        devel
Summary:        Development files for libnvme3
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package provides header files to include and libraries to link with
for libnvme3.

%package        doc
Summary:        Reference manual for libnvme3
License:        LGPL-2.1-or-later
BuildArch:      noarch

%description    doc
This package contains the libnvme3 API reference manual.

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
%license LICENSE LICENSES/LGPL-2.1-or-later.txt
%doc README.md
%{_sbindir}/nvme
%{_datadir}/bash-completion/completions/nvme
%{_datadir}/zsh/site-functions/_nvme
%dir %{_sysconfdir}/nvme
%{_sysconfdir}/nvme/nvme-fabrics.conf.sample
%{_prefix}/lib/NetworkManager/dispatcher.d/80-nvmf-connect-nbft.sh
%{_unitdir}/nvmefc-boot-connections.service
%{_unitdir}/nvmf-autoconnect.service
%{_unitdir}/nvmf-connect.target
%{_unitdir}/nvmf-connect@.service
%{_unitdir}/nvmf-connect-nbft.service
%{_udevrulesdir}/71-nvmf-hpe.rules
%{_udevrulesdir}/70-nvmf-autoconnect.rules
%{_udevrulesdir}/70-nvmf-keys.rules
%{_udevrulesdir}/70-nvmf-registry.rules
%{_udevrulesdir}/71-nvmf-netapp.rules
%{_udevrulesdir}/71-nvmf-vastdata.rules
%{_udevrulesdir}/65-persistent-net-nbft.rules
%{_mandir}/man1/nvme*
%{_mandir}/man5/nvme*
# libnvme3 libs
%{_libdir}/libnvme3.so.1*

%files devel
%{_includedir}/libnvme3/
%{_libdir}/libnvme3.so
%{_libdir}/pkgconfig/libnvme3.pc

%files doc
%license LICENSES/LGPL-2.1-or-later.txt
%{_mandir}/man2/*

%changelog
%autochangelog
