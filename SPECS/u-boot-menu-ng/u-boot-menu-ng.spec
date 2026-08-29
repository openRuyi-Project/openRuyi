# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Hangfan Li <lihangfan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0


Name:           u-boot-menu-ng
Version:        0.0.2
Release:        %autorelease
Summary:        BootMenu Generator for U-Boot
BuildArch:      noarch
License:        GPL-2.0-or-later
URL:            https://github.com/SalimTerryLi/u-boot-menu-ng
#!RemoteAsset:  sha256:005825316d8231e1f6d44ad104d1d2b6f30fd51188ef738532701bd27049c19d
Source0:        https://github.com/SalimTerryLi/u-boot-menu-ng/archive/refs/tags/v%{version}.tar.gz

%description
u-boot-menu-ng generates configuration loadable by u-boot.

%package     -n kernel-install-u-boot-menu-ng
Summary:        u-boot-menu plugin for kernel-install
Requires:       kernel-install
Requires:       u-boot-menu-ng = %{version}-%{release}

%description -n kernel-install-u-boot-menu-ng
u-boot-menu-ng plugin for kernel-install provided by systemd.

%prep
%autosetup -n u-boot-menu-ng-%{version}

%install
install -Dm 755 u-boot-update %{buildroot}%{_sbindir}/u-boot-update
install -Dm 644 config/u-boot %{buildroot}%{_sysconfdir}/default/u-boot
install -Dm 644 config/conf.d/50-distro-name.conf %{buildroot}%{_datadir}/u-boot-menu/conf.d/50-distro-name.conf
install -Dm 644 plugins/finder/bootdir.plugin %{buildroot}%{_datadir}/u-boot-menu/plugins/finder/bootdir.plugin
install -Dm 644 plugins/finder/modulesdir.plugin %{buildroot}%{_datadir}/u-boot-menu/plugins/finder/modulesdir.plugin
install -Dm 644 plugins/target/30-default.plugin %{buildroot}%{_datadir}/u-boot-menu/plugins/target/30-default.plugin
install -Dm 644 plugins/target/70-rescue.plugin %{buildroot}%{_datadir}/u-boot-menu/plugins/target/70-rescue.plugin
install -Dm 755 integration/kernel-install/90-u-boot-menu.install %{buildroot}%{_prefix}/lib/kernel/install.d/90-u-boot-menu.install

%files
%license COPYING
%{_sbindir}/u-boot-update
%{_datadir}/u-boot-menu
%config(noreplace) %{_sysconfdir}/default/u-boot

%files -n kernel-install-u-boot-menu-ng
%{_prefix}/lib/kernel/install.d/90-u-boot-menu.install

%changelog
%autochangelog
