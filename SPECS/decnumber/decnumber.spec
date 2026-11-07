# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           decnumber
Version:        3.68
Release:        %autorelease
Summary:        General Decimal Arithmetic library
License:        ICU
URL:            https://speleotrove.com/decimal/
#!RemoteAsset:  sha256:14ec2cf30b58758493a7661b78b80abfb281652b61a425b85cda83173518fe25
Source0:        https://speleotrove.com/decimal/decNumber-icu-368.zip
Source1:        CMakeLists.txt
Source2:        decnumber.pc.in
BuildSystem:    cmake

# Firebird's merged decimal conversion fixes.
Patch1000:      1000-fix-decimal-parsing-buffer-lifetime.patch

BuildRequires:  cmake
BuildRequires:  unzip

%description
decNumber implements decimal arithmetic, including the IEEE 754 decimal64
and decimal128 formats used for Firebird DECFLOAT values.

%package        devel
Summary:        Development files for decNumber
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers, the shared-library linker name, and pkg-config metadata for
applications using decNumber, decDouble, and decQuad.

%prep
%autosetup -N -n decNumber
# The upstream ZIP uses CRLF; normalize it before applying the source patch.
sed -i 's/\r$//' *.c *.h
%autopatch -p1
cp -p %{SOURCE1} %{SOURCE2} .

%files
%doc readme.txt
%license ICU-license.html
%{_libdir}/libdecNumber.so.*

%files devel
%doc decnumber.pdf
%{_includedir}/decnumber/
%{_libdir}/libdecNumber.so
%{_libdir}/pkgconfig/decnumber.pc

%changelog
%autochangelog
