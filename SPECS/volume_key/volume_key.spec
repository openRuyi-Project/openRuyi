# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           volume_key
Version:        0.3.12
Release:        %autorelease
Summary:        An utility for manipulating storage encryption keys and passphrases
License:        GPL-2.0-only AND (MPL-1.1 OR GPL-2.0-or-later OR LGPL-2.1-or-later)
URL:            https://pagure.io/volume_key/
VCS:            git:https://pagure.io/volume_key.git
#!RemoteAsset:  sha256:6ca3748fc1dad22c450bbf6601d4e706cb11c5e662d11bb4aeb473a9cd77309b
Source0:        https://releases.pagure.org/volume_key/volume_key-%{version}.tar.xz
BuildSystem:    autotools

BuildOption(conf):  --with-python=no
BuildOption(conf):  --with-python3=yes

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig(libcryptsetup)
BuildRequires:  gettext-devel
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gpgme)
BuildRequires:  pkgconfig(blkid)
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)

%description
The main goal of the software is to allow restoring access to an encrypted
hard drive if the primary user forgets the passphrase. This package provides
a command-line tool for manipulating storage volume encryption keys and
storing them separately from volumes.

%package        devel
Summary:        Development files for libvolume_key
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package provides libvolume_key, a library for manipulating storage volume
encryption keys and storing them separately from volumes.

%package     -n python-%{name}
Summary:        Python 3 bindings for lib%{name}
Requires:       %{name} = %{version}-%{release}
Provides:       python3-%{name}
%python_provide python3-%{name}

%description -n python-%{name}
This package contains Python 3 bindings for libvolume_key.

%conf -p
autoreconf -fiv

%install -a
# todo: fix the name error.
# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
%find_lang %{name} --generate-subpackages

# todo: the tests should on the real machine,we skip here.
%check

%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog NEWS
%{_bindir}/volume_key
%{_mandir}/man8/volume_key.8*
%{_libdir}/libvolume_key.so.*

%files devel
%{_includedir}/volume_key/
%{_libdir}/libvolume_key.so

%files -n python-volume_key
%{python3_sitearch}/_volume_key.so
%{python3_sitearch}/volume_key.py
%{python3_sitearch}/__pycache__/volume_key.*

%changelog
%autochangelog
