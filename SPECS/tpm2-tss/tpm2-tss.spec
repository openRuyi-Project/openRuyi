# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           tpm2-tss
Version:        4.1.3
Release:        %autorelease
Summary:        TPM2.0 Software Stack
License:        BSD-2-Clause
URL:            https://github.com/tpm2-software/tpm2-tss
#!RemoteAsset
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --disable-silent-rules
BuildOption(conf):  --with-udevrulesdir=%{_udevrulesdir}
BuildOption(conf):  --with-udevrulesprefix=%{udevrules_prefix}
BuildOption(conf):  --with-runstatedir=%{_rundir}
BuildOption(conf):  --with-tmpfilesdir=%{_tmpfilesdir}
BuildOption(conf):  --with-sysusersdir=%{_sysusersdir}

BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libgcrypt)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(openssl)

%description
tpm2-tss is a software stack supporting Trusted Platform Module(TPM) 2.0 system
APIs. It sits between TPM driver and applications, providing TPM2.0 specified
APIs for applications to access TPM module through kernel TPM drivers.

%package        devel
Summary:        Headers and libraries for building apps that use tpm2-tss
Requires:       %{name} = %{version}-%{release}

%description    devel
This package contains headers and libraries required to build applications that
use tpm2-tss.

%install -a
find %{buildroot}%{_libdir} -type f -name \*.la -delete

%files
%doc README.md CHANGELOG.md
%license LICENSE
%{_sysconfdir}/tpm2-tss/
%{_libdir}/libtss2-mu.so.0*
%{_libdir}/libtss2-sys.so.1*
%{_libdir}/libtss2-esys.so.0*
%{_libdir}/libtss2-policy.so.0*
%{_libdir}/libtss2-rc.so.0*
%{_libdir}/libtss2-tctildr.so.0*
%{_libdir}/libtss2-tcti-cmd.so.0*
%{_libdir}/libtss2-tcti-device.so.0*
%{_libdir}/libtss2-tcti-mssim.so.0*
%{_libdir}/libtss2-tcti-pcap.so.0*
%{_libdir}/libtss2-tcti-i2c-helper.so.0*
%{_libdir}/libtss2-tcti-spidev.so.0*
%{_libdir}/libtss2-tcti-spi-helper.so.0*
%{_libdir}/libtss2-tcti-spi-ltt2go.so.0*
%{_libdir}/libtss2-tcti-swtpm.so.0*
%{_sysusersdir}/tpm2-tss.conf
%{_udevrulesdir}/%{udevrules_prefix}tpm-udev.rules
%{_libdir}/libtss2-fapi.so.1*
%{_tmpfilesdir}/tpm2-tss-fapi.conf

%files devel
%{_includedir}/tss2/
%{_libdir}/libtss2-mu.so
%{_libdir}/libtss2-sys.so
%{_libdir}/libtss2-esys.so
%{_libdir}/libtss2-fapi.so
%{_libdir}/libtss2-policy.so
%{_libdir}/libtss2-rc.so
%{_libdir}/libtss2-tctildr.so
%{_libdir}/libtss2-tcti-cmd.so
%{_libdir}/libtss2-tcti-device.so
%{_libdir}/libtss2-tcti-mssim.so
%{_libdir}/libtss2-tcti-pcap.so
%{_libdir}/libtss2-tcti-i2c-helper.so
%{_libdir}/libtss2-tcti-spidev.so
%{_libdir}/libtss2-tcti-spi-helper.so
%{_libdir}/libtss2-tcti-spi-ltt2go.so
%{_libdir}/libtss2-tcti-swtpm.so
%{_libdir}/pkgconfig/tss2-mu.pc
%{_libdir}/pkgconfig/tss2-sys.pc
%{_libdir}/pkgconfig/tss2-esys.pc
%{_libdir}/pkgconfig/tss2-fapi.pc
%{_libdir}/pkgconfig/tss2-policy.pc
%{_libdir}/pkgconfig/tss2-rc.pc
%{_libdir}/pkgconfig/tss2-tctildr.pc
%{_libdir}/pkgconfig/tss2-tcti-cmd.pc
%{_libdir}/pkgconfig/tss2-tcti-device.pc
%{_libdir}/pkgconfig/tss2-tcti-mssim.pc
%{_libdir}/pkgconfig/tss2-tcti-pcap.pc
%{_libdir}/pkgconfig/tss2-tcti-i2c-helper.pc
%{_libdir}/pkgconfig/tss2-tcti-spidev.pc
%{_libdir}/pkgconfig/tss2-tcti-spi-helper.pc
%{_libdir}/pkgconfig/tss2-tcti-spi-ltt2go.pc
%{_libdir}/pkgconfig/tss2-tcti-swtpm.pc
%{_mandir}/man3/*.3.gz
%{_mandir}/man5/*.5.gz
%{_mandir}/man7/tss2*.7.gz

%changelog
%{?autochangelog}
