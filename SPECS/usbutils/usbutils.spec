# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Yafen Fang <yafen@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           usbutils
Version:        018
Release:        %autorelease
Summary:        Linux USB utilities
License:        GPL-2.0-or-later
URL:            http://www.linux-usb.org/
VCS:            git:https://git.kernel.org/pub/scm/linux/kernel/git/gregkh/usbutils.git
#!RemoteAsset
Source0:        https://www.kernel.org/pub/linux/utils/usb/usbutils/%{name}-%{version}.tar.xz
#!RemoteAsset
Source1:        https://www.kernel.org/pub/linux/utils/usb/usbutils/%{name}-%{version}.tar.sign

BuildSystem:    meson

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libudev)
Requires:       hwdata

%description
This is a collection of USB tools running on a USB host.

%install -a
rm -rf %{buildroot}/%{_libdir}/pkgconfig/usbutils.pc

%files
%license LICENSES/GPL*
%doc NEWS
%{_bindir}/*
%{_mandir}/man?/*

%changelog
%autochangelog
