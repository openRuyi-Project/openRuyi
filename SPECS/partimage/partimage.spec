# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jingkun Zheng <zhengjingkun@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           partimage
Version:        0.6.9
Release:        %autorelease
Summary:        Partition imaging and cloning tool
License:        GPL-2.0-or-later
URL:            https://www.partimage.org/
VCS:            git:https://gitlab.com/partimage/partimage-sources.git
#!RemoteAsset:  sha256:753a6c81f4be18033faed365320dc540fe5e58183eaadcd7a5b69b096fec6635
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# Local sysusers entry and the OpenSSL request configuration used to create
# the partimaged certificate.
Source1:        partimage.sysusers
Source2:        partimage-certs.cnf
BuildSystem:    autotools

# The three Debian patches below are still required with openRuyi's zlib 1.3,
# OpenSSL 3 and glibc 2.4x.  Without them the build fails on the gzFile type,
# on the removed CRYPTO_lock/SSLv2_client_method APIs, and on the makedev
# macro expansion respectively.
# https://bugs.debian.org/662596
Patch2000:      2000-Fix-gzFile-type-for-modern-zlib.patch
# https://bugs.debian.org/859549
Patch2001:      2001-Use-OpenSSL-3-compatible-API.patch
# https://bugs.debian.org/915987
Patch2002:      2002-Fix-makedev-macro-for-glibc-2.28.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(libnewt)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  systemd-rpm-macros

Requires:       e2fsprogs
Requires:       util-linux

%description
Partimage saves and restores partitions as image files. Only the used
blocks of a partition are copied, so an image is usually much smaller than
the partition itself. The image can be written to a file, to a set of
split files, or transferred to a partimaged server over the network.

%package        server
Summary:        Server daemon for partimage
Requires:       openssl
Requires(pre):  systemd-sysusers

%description    server
The partimaged daemon stores and serves partition images over the network.
Transfers are encrypted with SSL, and the daemon drops privileges to the
partimag user after startup.

%conf -p
autoreconf -fiv

%install -a
%find_lang %{name} --generate-subpackages
install -D -m 0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/partimage.conf
install -D -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/partimaged/partimage-certs.cnf
install -d -m 0750 %{buildroot}%{_localstatedir}/lib/partimaged
rm -rf %{buildroot}%{_docdir}/%{name}

%check
# Check if binaries can at least start
./src/client/partimage --version
./src/server/partimaged --version

%pre server
%sysusers_create_package %{name} %{SOURCE1}

%post server
# partimaged exits at startup when its certificate or key is missing, so
# create a self-signed pair from the shipped request configuration.  The
# pair is generated instead of shipped to keep a private key out of the
# package, and administrators can replace it with their own certificate.
# Debian does the same in its partimage-server postinst; see
# https://salsa.debian.org/debian/partimage/-/blob/master/debian/partimage-server.README.Debian
# and https://salsa.debian.org/debian/partimage/-/blob/master/debian/partimage-certs.cnf
if [ ! -s %{_sysconfdir}/partimaged/partimaged.cert ] ||
    [ ! -s %{_sysconfdir}/partimaged/partimaged.key ]; then
    %{_bindir}/openssl req -new -x509 -nodes \
        -config %{_sysconfdir}/partimaged/partimage-certs.cnf \
        -out %{_sysconfdir}/partimaged/partimaged.cert \
        -keyout %{_sysconfdir}/partimaged/partimaged.key 2>/dev/null || :
    chmod 0600 %{_sysconfdir}/partimaged/partimaged.key 2>/dev/null || :
    chmod 0600 %{_sysconfdir}/partimaged/partimaged.cert 2>/dev/null || :
    if [ -s %{_sysconfdir}/partimaged/partimaged.cert ]; then
        echo "partimaged: created a self-signed certificate valid for 30 days."
        echo "partimaged: reissue it before it expires, or install your own:"
        echo "  openssl req -new -x509 -nodes \\"
        echo "      -config %{_sysconfdir}/partimaged/partimage-certs.cnf \\"
        echo "      -out %{_sysconfdir}/partimaged/partimaged.cert \\"
        echo "      -keyout %{_sysconfdir}/partimaged/partimaged.key"
    else
        echo "partimaged: no SSL certificate; partimaged will not start until" >&2
        echo "partimaged: %{_sysconfdir}/partimaged/partimaged.cert exists" >&2
    fi
fi
if [ -d %{_localstatedir}/lib/partimaged ]; then
    chown partimag:partimag %{_localstatedir}/lib/partimaged || :
    chmod 0750 %{_localstatedir}/lib/partimaged || :
fi

%files -f %{name}.lang
%doc AUTHORS BUGS ChangeLog README
%license COPYING
%{_sbindir}/partimage

%files server
%config(noreplace) %{_sysconfdir}/partimaged/partimage-certs.cnf
%config(noreplace) %{_sysconfdir}/partimaged/partimagedusers
%doc README.partimaged
%dir %{_sysconfdir}/partimaged
%dir %attr(0750,partimag,partimag) %{_localstatedir}/lib/partimaged
%{_sbindir}/partimaged
%{_sysusersdir}/partimage.conf

%changelog
%autochangelog
