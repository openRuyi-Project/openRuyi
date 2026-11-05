# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           gnupg
Version:        2.5.24
Release:        %autorelease
Summary:        File encryption, decryption, signature creation and verification utility
License:        GPL-3.0-or-later
URL:            https://www.gnupg.org
VCS:            git:https://git.gnupg.org/gnupg.git
#!RemoteAsset:  sha256:bf149d01a2b9fcc0e4589b8ae8697d3d5c557ea48ed95a3fa55dd3b1187e6039
Source0:        https://gnupg.org/ftp/gcrypt/gnupg/gnupg-%{version}.tar.bz2
Source1:        scdaemon.udev
BuildSystem:    autotools

BuildOption(conf):  --enable-g13
BuildOption(conf):  --enable-large-secmem
BuildOption(conf):  --with-gnu-ld
BuildOption(conf):  --with-default-trust-store-file=%{_sysconfdir}/pki/ca-trust/extracted/pem/tls-ca-bundle.pem

BuildRequires:  expect
BuildRequires:  fdupes
BuildRequires:  texinfo
BuildRequires:  pkgconfig(npth)
BuildRequires:  pkgconfig(ldap)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(libassuan) >= 3.0.0
BuildRequires:  glibc-devel
BuildRequires:  pkgconfig(libgcrypt) >= 1.12.0
BuildRequires:  libgpg-error-devel >= 1.56
BuildRequires:  pkgconfig(ksba)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(zlib)

Requires:       pinentry
Requires:       libgcrypt >= 1.12.0

Recommends:     dirmngr = %{version}-%{release}

%description
GnuPG is a hybrid-encryption software program for encrypting/decrypting
messages and/or signing and verifying them.

%package     -n dirmngr
Summary:        Keyserver, CRL, and OCSP access for GnuPG
Requires:       ca-certificates
Requires:       libgcrypt >= 1.12.0

%description -n dirmngr
Dirmngr handles access to OpenPGP keyservers, CRLs, and OCSP providers
for GnuPG. It is invoked internally by gpg and gpgsm.

%package        scdaemon
Summary:        GnuPG SmartCard daemon
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    scdaemon
GnuPG is GNU's tool for secure communication and data storage. This
package contains the SmartCard daemon.

%install -a
install -Dm 0644 %{SOURCE1} %{buildroot}%{_udevrulesdir}/60-scdaemon.rules

%find_lang gnupg2 --generate-subpackages

%fdupes -s %{buildroot}

%post
%udev_rules_update

%files -f gnupg2.lang
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
%exclude %{_bindir}/gpg-card
%exclude %{_libexecdir}/gpg-auth
%exclude %{_libexecdir}/scdaemon
%exclude %{_mandir}/man?/gpg-card.*
%exclude %{_mandir}/man?/scdaemon.*

%files -n dirmngr
%{_mandir}/*/dirmngr*%{?ext_man}
%{_bindir}/dirmngr*
%{_libexecdir}/dirmngr_ldap

%files scdaemon
%{_bindir}/gpg-card
%{_libexecdir}/gpg-auth
%{_libexecdir}/scdaemon
%{_mandir}/man?/gpg-card.*
%{_mandir}/man?/scdaemon.*

%changelog
%autochangelog
