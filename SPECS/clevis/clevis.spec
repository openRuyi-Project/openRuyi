# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Jingkun Zheng <zhengjingkun@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           clevis
Version:        23
Release:        %autorelease
Summary:        Automated decryption framework
License:        GPL-3.0-or-later
URL:            https://github.com/latchset/clevis
#!RemoteAsset:  sha256:a8a09f148d54d91aa0d21c5fa508dd1446c2a200be7679fbf6e7d19196aec164
Source0:        https://github.com/latchset/clevis/archive/refs/tags/v%{version}.tar.gz
Source1:        clevis.sysusers
BuildSystem:    meson

BuildOption(conf):  -Duser=clevis
BuildOption(conf):  -Dgroup=clevis
BuildOption(conf):  -Dtpm1=disabled
%ifarch riscv64
BuildOption(check):  --timeout-multiplier 2
%endif

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  ninja
BuildRequires:  bash-completion
BuildRequires:  pkgconfig
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
BuildRequires:  dracut
BuildRequires:  pkgconfig(jose)
BuildRequires:  audit-devel
BuildRequires:  pkgconfig(udisks2)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(libcryptsetup)
BuildRequires:  pkgconfig(luksmeta)
BuildRequires:  cryptsetup
BuildRequires:  curl

Requires:       coreutils
Requires:       jose >= 8
Requires:       curl
Requires:       cryptsetup
Requires:       luksmeta >= 8
Requires:       openssl

%description
Clevis is a framework for automated decryption. It allows you to encrypt
data using sophisticated unlocking policies which enable decryption to
occur automatically.

%install -a
install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/clevis.conf

%pre
%sysusers_create_package %{name} %{SOURCE1}

%post
%systemd_post clevis-luks-askpass.path

%preun
%systemd_preun clevis-luks-askpass.path

%postun
%systemd_postun clevis-luks-askpass.path

%files
%license COPYING
%{_bindir}/clevis*
%{_sysusersdir}/clevis.conf
%{_libexecdir}/clevis-luks-askpass
%{_unitdir}/clevis-luks-askpass.path
%{_unitdir}/clevis-luks-askpass.service
%dir %{_prefix}/lib/dracut/modules.d/50clevis*
%{_prefix}/lib/dracut/modules.d/50clevis/*
%{_sysconfdir}/xdg/autostart/clevis-luks-udisks2.desktop
%attr(4755, root, root) %{_libexecdir}/%{name}-luks-udisks2
%{_libexecdir}/clevis-luks-pkcs11-*
%{_unitdir}/clevis-luks-pkcs11-askpass.service
%{_unitdir}/clevis-luks-pkcs11-askpass.socket
%{_prefix}/lib/dracut/modules.d/50clevis-pin-pkcs11/*
%{_prefix}/lib/dracut/modules.d/50clevis-pin-null/module-setup.sh
%{_prefix}/lib/dracut/modules.d/50clevis-pin-sss/module-setup.sh
%{_prefix}/lib/dracut/modules.d/50clevis-pin-tang/module-setup.sh
%{_prefix}/lib/dracut/modules.d/50clevis-pin-tpm2/module-setup.sh
%{_prefix}/lib/dracut/modules.d/50clevis-pin-file/module-setup.sh

%changelog
%autochangelog
