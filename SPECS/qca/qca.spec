# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           qca
Summary:        Qt6 Cryptographic Architecture
Version:        2.3.10
Release:        %autorelease
License:        LGPL-2.1-only
URL:            https://invent.kde.org/libraries/qca
#!RemoteAsset:  sha256:1c5b722da93d559365719226bb121c726ec3c0dc4c67dea34f1e50e4e0d14a02
Source0:        https://download.kde.org/stable/qca/%{version}/qca-%{version}.tar.xz
BuildSystem:    cmake

BuildOption(conf):  -DQT6=ON
BuildOption(conf):  -DQCA_INSTALL_IN_QT_PREFIX=ON
BuildOption(conf):  -DQCA_BINARY_INSTALL_DIR=%{_bindir}
BuildOption(conf):  -DQCA_MAN_INSTALL_DIR=%{_mandir}
BuildOption(conf):  -DQCA_INCLUDE_INSTALL_DIR=%{_qt6_includedir}
BuildOption(conf):  -DQCA_PRIVATE_INCLUDE_INSTALL_DIR=%{_qt6_includedir}
BuildOption(conf):  -DWITH_botan_PLUGIN=OFF
BuildOption(conf):  -DWITH_gcrypt_PLUGIN=ON
BuildOption(conf):  -DWITH_gnupg_PLUGIN=ON
BuildOption(conf):  -DWITH_logger_PLUGIN=ON
BuildOption(conf):  -DWITH_nss_PLUGIN=ON
BuildOption(conf):  -DWITH_ossl_PLUGIN=ON
BuildOption(conf):  -DWITH_pkcs11_PLUGIN=OFF
BuildOption(conf):  -DWITH_softstore_PLUGIN=ON
BuildOption(conf):  -DWITH_cyrus_sasl_PLUGIN=ON
BuildOption(conf):  -DQt6_FOUND=TRUE
BuildOption(conf):  -DBUILD_TESTS=ON

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  qt6-macros
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  pkgconfig(libgcrypt)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(libsasl2)

%description
Taking a hint from the similarly-named Java Cryptography Architecture,
QCA aims to provide a straightforward and cross-platform crypto API,
using Qt datatypes and conventions. This package provides the Qt6 version.

%package        devel
Summary:        Qt6 Cryptographic Architecture development files
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(Qt6Core)

%description    devel
Development files for QCA-Qt6.

%check
export CTEST_OUTPUT_ON_FAILURE=1
export PKG_CONFIG_PATH=%{buildroot}%{_libdir}/pkgconfig
%ctest

%files
%license COPYING
%doc README TODO
%{_bindir}/mozcerts-qt6
%{_bindir}/qcatool-qt6
%{_mandir}/man1/qcatool-qt6.1*
%{_qt6_libdir}/libqca-qt6.so.2*
%dir %{_qt6_pluginsdir}/crypto/
%{_qt6_pluginsdir}/crypto/libqca-cyrus-sasl.so
%{_qt6_pluginsdir}/crypto/libqca-gcrypt.so
%{_qt6_pluginsdir}/crypto/libqca-gnupg.so
%{_qt6_pluginsdir}/crypto/libqca-logger.so
%{_qt6_pluginsdir}/crypto/libqca-nss.so
%{_qt6_pluginsdir}/crypto/libqca-ossl.so
%{_qt6_pluginsdir}/crypto/libqca-softstore.so
%{_prefix}/certs/rootcerts.pem

%files devel
%{_qt6_includedir}/QtCrypto
%{_qt6_libdir}/libqca-qt6.so
%{_libdir}/cmake/Qca-qt6/

%changelog
%autochangelog
