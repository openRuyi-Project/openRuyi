# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# TODO: better way to keep opendnssec and softhsm versions in sync
%global opendnssec_ver 2.1.14

Name:           softhsm
Version:        2.6.1
Release:        %autorelease
Summary:        Software version of a PKCS#11 Hardware Security Module
License:        BSD-2-clause
URL:            https://www.opendnssec.org/
VCS:            git:https://github.com/softhsm/SoftHSMv2
#!RemoteAsset:  sha256:61249473054bcd1811519ef9a989a880a7bdcc36d317c9c25457fc614df475f2
Source0:        https://github.com/opendnssec/opendnssec/releases/download/%{opendnssec_ver}/%{name}-%{version}.tar.gz
Source1:        softhsm.sysusers
BuildSystem:    autotools

# https://github.com/softhsm/SoftHSMv2/pull/633
Patch0:         0001-fix-openssl3-tests.patch
# https://github.com/softhsm/SoftHSMv2/pull/742
Patch1:         0002-prevent-global-deleted-objects-access.patch

BuildOption(conf):  --libdir=%{_libdir}/pkcs11
BuildOption(conf):  --with-openssl=%{_prefix}
BuildOption(conf):  --enable-ecc
BuildOption(conf):  --enable-eddsa
BuildOption(conf):  --disable-gost
BuildOption(conf):  --with-migrate
BuildOption(conf):  --enable-visibility
BuildOption(conf):  --with-p11-kit=%{_datadir}/p11-kit/modules

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(cppunit)
BuildRequires:  p11-kit-devel

Requires:       p11-kit

%description
OpenDNSSEC is providing a software implementation of a generic
cryptographic device with a PKCS#11 interface, the SoftHSM. SoftHSM is
designed to meet the requirements of OpenDNSSEC, but can also work together
with other cryptographic products because of the PKCS#11 interface.

%package        devel
Summary:        Development package of softhsm
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(openssl)
Requires:       pkgconfig(sqlite3)

%description    devel
The devel package contains the libsofthsm include files

%conf -p
autoreconf -fiv

%conf -a
# remove softhsm/ subdir auto-added to --libdir
sed -i 's:full_libdir/softhsm:full_libdir:g' configure

%build -p
# This package fails its testsuite with LTO enabled and needs further
# investigation
%define _lto_cflags %{nil}

%install -a
rm %{buildroot}/%{_sysconfdir}/softhsm2.conf.sample
rm -f %{buildroot}/%{_libdir}/pkcs11/*a
mkdir -p %{buildroot}%{_includedir}/softhsm
cp src/lib/*.h %{buildroot}%{_includedir}/softhsm
mkdir -p %{buildroot}/%{_sharedstatedir}/softhsm/tokens

# leave a softlink where softhsm-1 installed its library. Programs like
# opendnssec have that filename in their configuration file.
mkdir -p %{buildroot}%{_libdir}/softhsm/
ln -s ../pkcs11/libsofthsm2.so %{buildroot}%{_libdir}/softhsm/libsofthsm.so
# Also NSS needs it to be in the search path too
ln -s ../pkcs11/libsofthsm2.so %{buildroot}%{_libdir}/libsofthsm2.so

install -D %{SOURCE1} %{buildroot}%{_sysusersdir}/%{name}.conf

%check
for d in crypto data_mgr handle_mgr object_store session_mgr slot_mgr ; do
make check  -C src/lib/$d
done

pushd src/lib/test
make p11test
for t in TokenTests AsymWrapUnwrapTests DigestTests ForkTests \
         InitTests InfoTests SessionTests UserTests RandomTests \
         SignVerifyTests AsymEncryptDecryptTests DeriveTests \
         ObjectTests SymmetricAlgorithmTests ; do
./p11test $t
done
popd

%pre
%sysusers_create_package %{name} %{SOURCE1}

%files
%doc README.md FIPS-NOTES.md NEWS
%license LICENSE
%config(noreplace) %{_sysconfdir}/softhsm2.conf
%{_bindir}/*
%dir %{_libdir}/softhsm
%{_libdir}/pkcs11/libsofthsm2.so
%{_libdir}/libsofthsm2.so
%{_libdir}/softhsm/libsofthsm.so
%{_datadir}/p11-kit/modules/softhsm2.module
%attr(0750,ods,ods) %dir %{_sharedstatedir}/softhsm
%attr(1770,ods,ods) %dir %{_sharedstatedir}/softhsm/tokens
%doc LICENSE README.md NEWS
%{_mandir}/*/*
%{_sysusersdir}/%{name}.conf

%files devel
%attr(0755,root,root) %dir %{_includedir}/softhsm
%{_includedir}/softhsm/*.h

%changelog
%{?autochangelog}
