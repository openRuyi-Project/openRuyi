# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: Jingwiw <wangjingwei@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "bootstrap"
%bcond bootstrap 1
%else
%bcond bootstrap 0
%endif

%bcond  static        0
# For -tests subpackage.
%bcond  tests         0
%bcond  doc           0
%bcond  man           0

%if "%{flavor}" == "bootstrap"
Name:           glib-bootstrap
%else
Name:           glib
%endif
Version:        2.87.1
Release:        %autorelease
Summary:        A core application building block and utility library
License:        LGPL-2.1-or-later
URL:            https://docs.gtk.org/glib/
VCS:            git:https://gitlab.gnome.org/GNOME/glib.git
#!RemoteAsset:  sha256:fc2ce0f948ee163f8adc5bdde2f38612b8a3f270022aa1b0d087cb9f1f0ac5c2
Source0:        https://download.gnome.org/sources/glib/2.87/glib-%{version}.tar.xz
BuildSystem:    meson

Patch0:         meson.build-Avoid-linking-with-libatomic-when-unneed.patch

# --- Declarative Build Options ---
# These options are derived directly from analyzing the meson.build files.
BuildOption(conf):  --default-library=%{?with_static:both}%{!?with_static:shared}
# Upstream recommendation: distros should disable glib_debug for production.
BuildOption(conf):  -Dglib_debug=disabled
# Use the upstream-provided multiarch support for helper binaries.
BuildOption(conf):  -Dmultiarch=true
BuildOption(conf):  -Dselinux=%{?with_bootstrap:disabled}%{!?with_bootstrap:enabled}
BuildOption(conf):  -Dlibmount=enabled
# Handle bootstrap mode by disabling features with circular/heavy dependencies.
BuildOption(conf):  -Dintrospection=%{?with_bootstrap:disabled}%{!?with_bootstrap:enabled}
BuildOption(conf):  -Dinstalled_tests=%{?with_tests:true}%{!?with_tests:false}
BuildOption(conf):  -Ddocumentation=%{?with_doc:true}%{!?with_doc:false}
BuildOption(conf):  -Ddtrace=disabled
BuildOption(conf):  -Dsystemtap=disabled
BuildOption(conf):  -Dsysprof=disabled
BuildOption(conf):  -Dman-pages=%{?with_man:enabled}%{!?with_man:disabled}
BuildOption(conf):  -Dxattr=true

BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  pkgconfig(libelf)
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(mount)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(libattr)
# Conditional dependencies, disabled during bootstrap
%if %{without bootstrap}
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(libselinux)
%endif
# Conditional dependencies for documentation
%if %{with doc}
BuildRequires:  pkgconfig(gi-docgen)
%endif
# Conditional dependencies for tests
%if %{with tests}
BuildRequires:  dbus-daemon
BuildRequires:  shared-mime-info
%endif
%if %{with man}
BuildRequires:  python3dist(docutils)
%endif
# For %check
BuildRequires:  systemd

%description
GLib is the low-level core library that forms the basis of GTK and GNOME.
It provides data structure handling for C, portability wrappers, and interfaces
for an event loop, threads, dynamic loading, and an object system.
This package contains the essential runtime libraries and tools.

%package        devel
Summary:        Development files for the GLib library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the header files, libraries, and developer tools
needed to build applications that use GLib.

%if %{with doc}
%package        doc
Summary:        Documentation for the GLib library
BuildArch:      noarch

%description    doc
This package contains the API documentation for the GLib library.
%endif

%if %{with tests}
%package        tests
Summary:        Tests for the GLib library
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    tests
Contains installed tests that can be used to verify the functionality
of the installed GLib package.
%endif

%install -a
# Fix broken absolute symlinks created by meson -Dmultiarch=true ---
rm -f %{buildroot}%{_bindir}/gio-querymodules
rm -f %{buildroot}%{_bindir}/glib-compile-schemas

ln -sf ../%{_lib}/glib-2.0/gio-querymodules %{buildroot}%{_bindir}/gio-querymodules
ln -sf ../%{_lib}/glib-2.0/glib-compile-schemas %{buildroot}%{_bindir}/glib-compile-schemas

# Avoid illegal package names
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/*@*
%find_lang glib20 --generate-subpackages --all-name

# handle GIO/GSettings cache updates.
%transfiletriggerin -- %{_libdir}/gio/modules
# Use the multiarch path for the query tool
%{_libdir}/glib-2.0/gio-querymodules %{_libdir}/gio/modules &> /dev/null || :

%transfiletriggerpostun -- %{_libdir}/gio/modules
%{_libdir}/glib-2.0/gio-querymodules %{_libdir}/gio/modules &> /dev/null || :

%transfiletriggerin -- %{_datadir}/glib-2.0/schemas
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%transfiletriggerpostun -- %{_datadir}/glib-2.0/schemas
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%check
# Avoid fragile tests failure.
%meson_test --timeout-multiplier 5 || cat %{_build}/meson-logs/testlog.txt

%files -f glib20.lang
%license LICENSES/LGPL-2.1-or-later.txt
%doc NEWS README.md
# Runtime libraries
%{_libdir}/libglib-2.0.so.*
%{_libdir}/libgthread-2.0.so.*
%{_libdir}/libgmodule-2.0.so.*
%{_libdir}/libgobject-2.0.so.*
%{_libdir}/libgio-2.0.so.*
%{_libdir}/libgirepository-2.0.so.*
%if %{without bootstrap}
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/*.typelib
%endif
# Runtime tools, data, and multiarch helpers
%{_bindir}/gio
%{_bindir}/gsettings
%{_bindir}/gdbus
%{_bindir}/gapplication
# Added: The symlink for glib-compile-schemas
%{_bindir}/glib-compile-schemas
# Added: The symlink for gio-querymodules
%{_bindir}/gio-querymodules
# The actual binaries installed by Meson with -Dmultiarch=true
%{_libdir}/glib-2.0/gio-querymodules
%{_libdir}/glib-2.0/glib-compile-schemas
%{_libdir}/glib-2.0/gio-launch-desktop
%{_datadir}/bash-completion/completions/gapplication
%{_datadir}/bash-completion/completions/gdbus
%{_datadir}/bash-completion/completions/gio
%{_datadir}/bash-completion/completions/gsettings

%files devel
%{_libdir}/lib*.so
%dir %{_libdir}/glib-2.0
%dir %{_libdir}/glib-2.0/include
%{_libdir}/glib-2.0/include/glibconfig.h
%{_includedir}/glib-2.0/
%{_includedir}/gio-unix-2.0/
%{_libdir}/pkgconfig/gio-2.0.pc
%{_libdir}/pkgconfig/gio-unix-2.0.pc
%{_libdir}/pkgconfig/girepository-2.0.pc
%{_libdir}/pkgconfig/glib-2.0.pc
%{_libdir}/pkgconfig/gmodule-2.0.pc
%{_libdir}/pkgconfig/gmodule-export-2.0.pc
%{_libdir}/pkgconfig/gmodule-no-export-2.0.pc
%{_libdir}/pkgconfig/gobject-2.0.pc
%{_libdir}/pkgconfig/gthread-2.0.pc
%{_datadir}/aclocal/*.m4
# Added: GDB helper scripts for better debugging experience
%dir %{_datadir}/gdb
%dir %{_datadir}/gdb/auto-load
%dir %{_datadir}/gdb/auto-load/usr
%dir %{_datadir}/gdb/auto-load/usr/%{_lib}
%{_datadir}/gdb/auto-load/usr/%{_lib}/libglib-2.0.so.*-gdb.py
%{_datadir}/gdb/auto-load/usr/%{_lib}/libgobject-2.0.so.*-gdb.py
# Added: gettext integration files
%dir %{_datadir}/gettext
%dir %{_datadir}/gettext/its
%{_datadir}/gettext/its/gschema.its
%{_datadir}/gettext/its/gschema.loc
# Added: codegen scripts, DTDs, and valgrind suppressions
%{_datadir}/glib-2.0/gdb/
%{_datadir}/glib-2.0/gettext/
%{_datadir}/glib-2.0/schemas/gschema.dtd
%{_datadir}/glib-2.0/codegen/
%{_datadir}/glib-2.0/dtds/
%{_datadir}/glib-2.0/valgrind/
%{_datadir}/bash-completion/completions/gresource
%if %{without bootstrap}
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/*.gir
%endif
# Devel tools
%{_bindir}/glib-genmarshal
%{_bindir}/glib-gettextize
%{_bindir}/glib-mkenums
%{_bindir}/gobject-query
%{_bindir}/gtester
# Added: gtester-report tool
%{_bindir}/gtester-report
%{_bindir}/gdbus-codegen
%{_bindir}/glib-compile-resources
%{_bindir}/gresource
%{_bindir}/gi-compile-repository
%{_bindir}/gi-decompile-typelib
%{_bindir}/gi-inspect-typelib

%if %{with doc}
%files doc
%{_datadir}/doc/glib-2.0/
%{_datadir}/doc/gobject-2.0/
%{_datadir}/doc/gio-2.0/
%endif

%if %{with tests}
%files tests
%{_libexecdir}/installed-tests/glib/
%{_datadir}/installed-tests/glib/
%endif

%changelog
%autochangelog
