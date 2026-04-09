# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           ima-evm-utils
Version:        1.6.2
Release:        %autorelease
Summary:        IMA/EVM support utilities
License:        GPL-2.0-or-later
URL:            https://github.com/linux-integrity/ima-evm-utils
VCS:            git:https://github.com/linux-integrity/ima-evm-utils
#!RemoteAsset
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-static

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  tpm2-tss-devel
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(libkeyutils)
# for tests.
BuildRequires:  xxd
BuildRequires:  e2fsprogs

%description
The Trusted Computing Group(TCG) run-time Integrity Measurement Architecture
(IMA) maintains a list of hash values of executables and other sensitive
system files, as they are read or executed. These are stored in the file
systems extended attributes. The Extended Verification Module (EVM) prevents
unauthorized changes to these extended attributes on the file system.
ima-evm-utils is used to prepare the file system for these extended attributes.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package provides the header files for %{name}

%conf -p
autoreconf -fiv

%install -a
rm -rf %{buildroot}%{_datadir}/doc

%files
%license LICENSES.txt COPYING
%doc NEWS README AUTHORS
%{_bindir}/evmctl
%{_libdir}/libimaevm.so.*

%files devel
%{_includedir}/imaevm.h
%{_libdir}/libimaevm.so

%changelog
%autochangelog
