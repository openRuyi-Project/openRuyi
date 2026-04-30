# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: jingyupu <pujingyu@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define kf6_version 6.19.0
%define qt6_version 6.9.0

Name:           signon-kwallet-extension
Version:        25.12.3
Release:        %autorelease
Summary:        KWallet integration for signon framework
License:        GPL-2.0-or-later
URL:            https://www.kde.org
VCS:            git:https://invent.kde.org/network/signon-kwallet-extension.git
#!RemoteAsset:  sha256:4fc7566893bf8dd0d6e236d52e13319c809642b7e85f6680bcfbad47888a4836
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DBUILD_WITH_QT6:BOOL=TRUE
BuildOption(conf):  -DBUILD_TESTING=OFF

BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6Wallet) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  pkgconfig(SignOnExtension)

Supplements:    signond

%description
KWallet integration for signon framework.

%install -a

%files
%license COPYING
%dir %{_kf6_libdir}/signon/extensions
%{_kf6_libdir}/signon/extensions/libkeyring-kwallet.so*

%changelog
%autochangelog
