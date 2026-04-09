# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           gnupg
Version:        2.5.16
Release:        %autorelease
Summary:        File encryption, decryption, signature creation and verification utility
License:        GPL-3.0-or-later
URL:            https://www.gnupg.org
VCS:            git:https://git.gnupg.org/gnupg.git
#!RemoteAsset:  sha256:05144040fedb828ced2a6bafa2c4a0479ee4cceacf3b6d68ccc75b175ac13b7e
Source0:        https://gnupg.org/ftp/gcrypt/gnupg/gnupg-%{version}.tar.bz2
Source1:        scdaemon.udev
BuildSystem:    autotools

BuildOption(conf):  --disable-rpath
BuildOption(conf):  --enable-g13
BuildOption(conf):  --enable-large-secmem
BuildOption(conf):  --with-gnu-ld
BuildOption(conf):  --with-default-trust-store-file=%{_sysconfdir}/ssl/ca-bundle.pem
BuildOption(conf):  --docdir=%{_docdir}/%{name}

BuildRequires:  expect
BuildRequires:  fdupes
BuildRequires:  texinfo
BuildRequires:  pkgconfig(npth)
BuildRequires:  pkgconfig(ldap)
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(libassuan)
BuildRequires:  glibc-devel
BuildRequires:  pkgconfig(libgcrypt)
BuildRequires:  libgpg-error-devel >= 1.56
BuildRequires:  pkgconfig(ksba)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(zlib)

Requires:       pinentry

Recommends:     dirmngr = %{version}-%{release}

%description
GnuPG is a hybrid-encryption software program for encrypting/decrypting
messages and/or signing and verifying them.

%package     -n dirmngr
Summary:        Keyserver, CRL, and OCSP access for GnuPG

%description -n dirmngr
Dirmngr handles access to OpenPGP keyservers, CRLs, and OCSP providers
for GnuPG. It is invoked internally by gpg and gpgsm.

%install -a
install -Dm 0644 %{SOURCE1} %{buildroot}%{_udevrulesdir}/60-scdaemon.rules
install -d -m 755 %{buildroot}%{_userunitdir}
# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*

%find_lang gnupg2 --generate-subpackages

%fdupes -s %{buildroot}

%post
%udev_rules_update

%files
%{_mandir}/*/[aghsw]*%{?ext_man}
%license COPYING*
%doc AUTHORS NEWS THANKS TODO ChangeLog
%{_infodir}/gnupg*
%doc %{_docdir}/%{name}
%{_bindir}/[gkw]*
%{_libexecdir}/[gks]*
%{_sbindir}/addgnupghome
%{_sbindir}/applygnupgdefaults
%{_sbindir}/g13-syshelp
%{_udevrulesdir}/60-scdaemon.rules
%{_datadir}/gnupg

%files -n dirmngr
%{_mandir}/*/dirmngr*%{?ext_man}
%{_bindir}/dirmngr*
%{_libexecdir}/dirmngr_ldap

%changelog
%autochangelog
