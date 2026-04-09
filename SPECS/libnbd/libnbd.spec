# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: sunyuechi <sunyuechi@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# The source directory.
%global source_directory 1.23-development

# The Python module happens to be called lib*.so.  Don't scan it and
# have a bogus "Provides: libnbdmod.*".
%global __provides_exclude_from ^%{python3_sitearch}/lib.*\\.so

Name:           libnbd
Version:        1.23.13
Release:        %autorelease
Summary:        NBD client library in userspace
License:        LGPL-2.0-or-later AND BSD-3-Clause
URL:            https://gitlab.com/nbdkit/libnbd
#!RemoteAsset
Source0:        http://libguestfs.org/download/libnbd/%{source_directory}/%{name}-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf):  --disable-static
BuildOption(conf):  --with-extra='%{name}-%{version}-%{release}'
BuildOption(conf):  --with-tls-priority=@LIBNBD,SYSTEM
BuildOption(conf):  --with-bash-completions
BuildOption(conf):  PYTHON=%{__python3}
BuildOption(conf):  --enable-python
BuildOption(conf):  --disable-ocaml
BuildOption(conf):  --enable-fuse
BuildOption(conf):  --disable-golang
BuildOption(conf):  --disable-rust
BuildOption(conf):  --disable-ublk

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
# For the core library.
BuildRequires:  make
BuildRequires:  perl
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(libxml-2.0)
# For nbdfuse.
BuildRequires:  fuse3
BuildRequires:  pkgconfig(fuse3)
# For the Python bindings.
BuildRequires:  pkgconfig(python3)
# For bash-completion.
BuildRequires:  bash-completion
BuildRequires:  pkgconfig(bash-completion)
# Only for running the test suite.
BuildRequires:  coreutils
BuildRequires:  util-linux

Recommends:     bash-completion
Recommends:     fuse3

%description
NBD — Network Block Device — is a protocol for accessing Block Devices
(hard disks and disk-like things) over a Network.

This is the NBD client library in userspace, a simple library for
writing NBD clients.

The key features are:

 * Synchronous and asynchronous APIs, both for ease of use and for
   writing non-blocking, multithreaded clients.

 * High performance.

 * Minimal dependencies for the basic library.

 * Well-documented, stable API.

 * Bindings in several programming languages.

%package        devel
Summary:        Development headers for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains development headers for %{name}.

%package        -n python-%{name}
Summary:        Python bindings for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       python3-%{name}
%python_provide python3-%{name}

%description    -n python-%{name}
python-%{name} contains Python bindings for %{name}.

%install -a
# Delete the golang man page since we're not distributing the bindings.
rm %{buildroot}%{_mandir}/man3/libnbd-golang.3*
rm %{buildroot}%{_mandir}/man3/libnbd-ocaml.3*

%files
%doc README.md
%license COPYING.LIB
%{_bindir}/nbdcopy
%{_bindir}/nbddump
%{_bindir}/nbdinfo
%{_libdir}/libnbd.so.*
%{_mandir}/man1/nbdcopy.1*
%{_mandir}/man1/nbddump.1*
%{_mandir}/man1/nbdinfo.1*
%{_bindir}/nbdfuse
%{_mandir}/man1/nbdfuse.1*
%{bash_completions_dir}/nbdcopy
%{bash_completions_dir}/nbddiscard
%{bash_completions_dir}/nbddump
%{bash_completions_dir}/nbdfuse
%{bash_completions_dir}/nbdinfo
%{bash_completions_dir}/nbdsh
%{bash_completions_dir}/nbdzero

%files devel
%doc TODO examples/*.c
%license examples/LICENSE-FOR-EXAMPLES
%{_includedir}/libnbd.h
%{_libdir}/libnbd.so
%{_libdir}/pkgconfig/libnbd.pc
%{_mandir}/man3/libnbd.3*
%{_mandir}/man1/libnbd-release-notes-1.*.1*
%{_mandir}/man3/libnbd-security.3*
%{_mandir}/man3/nbd_*.3*

%files -n python-%{name}
%{python3_sitearch}/libnbdmod*.so
%{python3_sitearch}/nbd.py
%{python3_sitearch}/nbdsh.py
%{_bindir}/nbddiscard
%{_bindir}/nbdsh
%{_bindir}/nbdzero
%{_mandir}/man1/nbddiscard.1*
%{_mandir}/man1/nbdsh.1*
%{_mandir}/man1/nbdzero.1*
%{_mandir}/man3/libnbd-python.3*

%changelog
%autochangelog
