# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           rhash
Version:        1.4.6
Release:        %autorelease
Summary:        Recursive Hasher
License:        0BSD
URL:            https://github.com/rhash/RHash
#!RemoteAsset
Source:        https://github.com/rhash/RHash/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:    autotools
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(openssl)

BuildOption(prep): -n RHash-%{version}
BuildOption(install): install-lib-so-link
BuildOption(install): install-lib-headers
BuildOption(install): install-gmo

%description
RHash (Recurcive Hasher) is a console utility for computing and
verifying magnet links and hash sums of files.
It supports CRC32, MD4, MD5, SHA1/SHA2, Tiger, DC++ TTH, BitTorrent
BTIH, AICH, eDonkey hash, GOST R 34.11-94, RIPEMD-160, HAS-160, EDON-R,
Whirlpool and Snefru hash algorithms. Hash sums are used to ensure and
verify integrity of large volumes of data for a long-term storing or
transferring.

Program features:
 * Calculation of Magnet links and EDonkey 2000 links.
 * Output in a predefined (SFV, BSD-like) or a user-defined format.
 * Updating crc files (adding hash sums of files missing in the crc
   file).
 * Ability to process directories recursively.

%package devel
Summary:        Headers and Static Library for LibRHash

%description devel
LibRHash is a professional, portable, thread-safe C library for
computing a wide variety of hash sums, such as CRC32, MD4, MD5, SHA1,
SHA256, SHA512, AICH, ED2K, Tiger, DC++ TTH, BitTorrent BTIH, GOST R
34.11-94, RIPEMD-160 HAS-160, EDON-R, Whirlpool and Snefru.
Hash sums are used to ensure and verify integrity of large volumes of
data for a long-term storing or transferring.

This package includes LibRHash development files.

%lang_package

%conf
# repleace unwanted fomit-frame pointer with desirable optflags
sed -i "s|-fomit-frame-pointer|%{optflags}|g" configure
# not a autotools configure
./configure \
  --prefix=%{_prefix} \
  --libdir=%{_libdir} \
  --sysconfdir=%{_sysconfdir} \
  --enable-lib-shared \
  --enable-gettext

%install -a
%find_lang %{name} %{?no_lang_C}

%files
%license COPYING
%doc ChangeLog README.md
%config(noreplace) %{_sysconfdir}/rhashrc
%{_bindir}/ed2k-link
%{_bindir}/edonr256-hash
%{_bindir}/edonr512-hash
%{_bindir}/gost12-256-hash
%{_bindir}/gost12-512-hash
%{_bindir}/has160-hash
%{_bindir}/magnet-link
%{_bindir}/rhash
%{_bindir}/sfv-hash
%{_bindir}/tiger-hash
%{_bindir}/tth-hash
%{_bindir}/whirlpool-hash
%{_mandir}/man1/ed2k-link.1%{?ext_man}
%{_mandir}/man1/edonr256-hash.1%{?ext_man}
%{_mandir}/man1/edonr512-hash.1%{?ext_man}
%{_mandir}/man1/gost12-256-hash.1%{?ext_man}
%{_mandir}/man1/gost12-512-hash.1%{?ext_man}
%{_mandir}/man1/has160-hash.1%{?ext_man}
%{_mandir}/man1/magnet-link.1%{?ext_man}
%{_mandir}/man1/rhash.1%{?ext_man}
%{_mandir}/man1/sfv-hash.1%{?ext_man}
%{_mandir}/man1/tiger-hash.1%{?ext_man}
%{_mandir}/man1/tth-hash.1%{?ext_man}
%{_mandir}/man1/whirlpool-hash.1%{?ext_man}
%{_libdir}/librhash.so.*

%files devel
%license COPYING
%doc ChangeLog README.md
%{_includedir}/rhash.h
%{_includedir}/rhash_torrent.h
%{_libdir}/librhash.so

%files lang -f %{name}.lang

%changelog
%{?autochangelog}
