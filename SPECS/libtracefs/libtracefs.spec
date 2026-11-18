# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           libtracefs
Version:        1.8.4
Release:        %autorelease
Summary:        Linux kernel trace file system library
License:        LGPL-2.1-only AND GPL-2.0-or-later
URL:            https://git.kernel.org/pub/scm/libs/libtrace/libtracefs.git
#!RemoteAsset:  sha256:75187bad93e622c94c4a691173e45f08948d38b9a28e9b855b54a3e956d289a6
Source0:        https://git.kernel.org/pub/scm/libs/libtrace/libtracefs.git/snapshot/%{name}-%{version}.tar.gz
BuildSystem:    meson

BuildOption(conf):  -Dhtmldir=%{_docdir}/%{name}-doc

BuildRequires:  asciidoc
BuildRequires:  bison
BuildRequires:  docbook-dtds
BuildRequires:  docbook-xsl
BuildRequires:  flex
BuildRequires:  meson
BuildRequires:  pkgconfig(cunit)
BuildRequires:  pkgconfig(libtraceevent)
BuildRequires:  xmlto

%description
The libtracefs library provides a C API to access and manipulate the Linux
kernel tracefs and tracing filesystems.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(libtraceevent)

%description    devel
This package provides the header files, libraries, and pkg-config metadata
needed to develop applications that use %{name}.

%package        doc
Summary:        HTML documentation for %{name}
BuildArch:      noarch

%description    doc
This package contains HTML documentation for the %{name} API.

%build -a
meson compile -C %{_vpath_builddir} docs

%install -a
rm -f %{buildroot}%{_libdir}/*.a

%check
# Upstream trace-utest requires a writable mounted tracefs (/sys/kernel/tracing)
# and kernel tracing permissions unavailable in the OBS buildroot.

%files
%doc README
%license LICENSES/LGPL-2.1 LICENSES/GPL-2.0
%{_bindir}/sqlhist
%{_libdir}/libtracefs.so.*
%{_datadir}/bash-completion/completions/tracefs_sql.bash
%{_mandir}/man1/*.1*

%files devel
%{_includedir}/libtracefs/
%{_libdir}/libtracefs.so
%{_libdir}/pkgconfig/libtracefs.pc
%{_mandir}/man3/*.3*

%files doc
%{_docdir}/libtracefs-doc/

%changelog
%autochangelog
