# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name objc2-app-kit
%global full_version 0.2.2
%global pkgname objc2-app-kit-0.2

Name:           rust-objc2-app-kit-0.2
Version:        0.2.2
Release:        %autorelease
Summary:        Rust crate "objc2-app-kit"
License:        MIT
URL:            https://github.com/madsmtm/objc2
#!RemoteAsset:  sha256:e4e89ad9e3d7d297152b17d39ed92cd50ca8063a89a9fa569046d41568891eff
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(objc2-0.5) >= 0.5.2
Requires:       crate(objc2-foundation-0.2) >= 0.2.2
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/appkitdefines) = %{version}
Provides:       crate(%{pkgname}/appkiterrors) = %{version}
Provides:       crate(%{pkgname}/apple) = %{version}
Provides:       crate(%{pkgname}/nscolorsampler) = %{version}
Provides:       crate(%{pkgname}/nshapticfeedback) = %{version}
Provides:       crate(%{pkgname}/nsnibdeclarations) = %{version}
Provides:       crate(%{pkgname}/nsnibloading) = %{version}
Provides:       crate(%{pkgname}/nsopengl) = %{version}
Provides:       crate(%{pkgname}/nsopengllayer) = %{version}
Provides:       crate(%{pkgname}/nsopenglview) = %{version}
Provides:       crate(%{pkgname}/nspressureconfiguration) = %{version}
Provides:       crate(%{pkgname}/nsspellprotocol) = %{version}
Provides:       crate(%{pkgname}/nstableviewdiffabledatasource) = %{version}
Provides:       crate(%{pkgname}/nsuserinterfacelayout) = %{version}
Provides:       crate(%{pkgname}/nsuserinterfacevalidation) = %{version}

%description
Source code for takopackized Rust crate "objc2-app-kit"

%package     -n %{name}+nsatstypesetter
Summary:        Bindings to the AppKit framework - feature "NSATSTypesetter"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsattributedstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsrange) >= 0.2.2
Provides:       crate(%{pkgname}/nsatstypesetter) = %{version}

%description -n %{name}+nsatstypesetter
This metapackage enables feature "NSATSTypesetter" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsaccessibility
Summary:        Bindings to the AppKit framework - feature "NSAccessibility"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsnotification) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nsaccessibility) = %{version}

%description -n %{name}+nsaccessibility
This metapackage enables feature "NSAccessibility" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsaccessibilitycolor
Summary:        Bindings to the AppKit framework - feature "NSAccessibilityColor" and 5 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nsaccessibilitycolor) = %{version}
Provides:       crate(%{pkgname}/nsaccessibilitycustomaction) = %{version}
Provides:       crate(%{pkgname}/nsinterfacestyle) = %{version}
Provides:       crate(%{pkgname}/nsstoryboardsegue) = %{version}
Provides:       crate(%{pkgname}/nstextcontent) = %{version}
Provides:       crate(%{pkgname}/nsuserinterfaceitemidentification) = %{version}

%description -n %{name}+nsaccessibilitycolor
This metapackage enables feature "NSAccessibilityColor" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "NSAccessibilityCustomAction", "NSInterfaceStyle", "NSStoryboardSegue", "NSTextContent", and "NSUserInterfaceItemIdentification" features.

%package     -n %{name}+nsaccessibilityconstants
Summary:        Bindings to the AppKit framework - feature "NSAccessibilityConstants"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsattributedstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nsaccessibilityconstants) = %{version}

%description -n %{name}+nsaccessibilityconstants
This metapackage enables feature "NSAccessibilityConstants" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsaccessibilitycustomrotor
Summary:        Bindings to the AppKit framework - feature "NSAccessibilityCustomRotor"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsrange) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nsaccessibilitycustomrotor) = %{version}

%description -n %{name}+nsaccessibilitycustomrotor
This metapackage enables feature "NSAccessibilityCustomRotor" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsaccessibilityelement
Summary:        Bindings to the AppKit framework - feature "NSAccessibilityElement" and 4 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nsaccessibilityelement) = %{version}
Provides:       crate(%{pkgname}/nscolorpicker) = %{version}
Provides:       crate(%{pkgname}/nscolorpicking) = %{version}
Provides:       crate(%{pkgname}/nsdocktile) = %{version}
Provides:       crate(%{pkgname}/nsgraphics) = %{version}

%description -n %{name}+nsaccessibilityelement
This metapackage enables feature "NSAccessibilityElement" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "NSColorPicker", "NSColorPicking", "NSDockTile", and "NSGraphics" features.

%package     -n %{name}+nsaccessibilityprotocols
Summary:        Bindings to the AppKit framework - feature "NSAccessibilityProtocols"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsattributedstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdata) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsrange) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsurl) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsvalue) >= 0.2.2
Provides:       crate(%{pkgname}/nsaccessibilityprotocols) = %{version}

%description -n %{name}+nsaccessibilityprotocols
This metapackage enables feature "NSAccessibilityProtocols" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsactioncell
Summary:        Bindings to the AppKit framework - feature "NSActionCell" and 7 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nsactioncell) = %{version}
Provides:       crate(%{pkgname}/nsbrowsercell) = %{version}
Provides:       crate(%{pkgname}/nsbuttontouchbaritem) = %{version}
Provides:       crate(%{pkgname}/nscustomtouchbaritem) = %{version}
Provides:       crate(%{pkgname}/nsimagecell) = %{version}
Provides:       crate(%{pkgname}/nspopovertouchbaritem) = %{version}
Provides:       crate(%{pkgname}/nssteppercell) = %{version}
Provides:       crate(%{pkgname}/nstouchbaritem) = %{version}

%description -n %{name}+nsactioncell
This metapackage enables feature "NSActionCell" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "NSBrowserCell", "NSButtonTouchBarItem", "NSCustomTouchBarItem", "NSImageCell", "NSPopoverTouchBarItem", "NSStepperCell", and "NSTouchBarItem" features.

%package     -n %{name}+nsaffinetransform
Summary:        Bindings to the AppKit framework - feature "NSAffineTransform"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsaffinetransform) >= 0.2.2
Provides:       crate(%{pkgname}/nsaffinetransform) = %{version}

%description -n %{name}+nsaffinetransform
This metapackage enables feature "NSAffineTransform" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsalert
Summary:        Bindings to the AppKit framework - feature "NSAlert"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nsalert) = %{version}

%description -n %{name}+nsalert
This metapackage enables feature "NSAlert" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsalignmentfeedbackfilter
Summary:        Bindings to the AppKit framework - feature "NSAlignmentFeedbackFilter"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Provides:       crate(%{pkgname}/nsalignmentfeedbackfilter) = %{version}

%description -n %{name}+nsalignmentfeedbackfilter
This metapackage enables feature "NSAlignmentFeedbackFilter" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsanimation
Summary:        Bindings to the AppKit framework - feature "NSAnimation"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdate) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsnotification) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobjcruntime) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsvalue) >= 0.2.2
Provides:       crate(%{pkgname}/nsanimation) = %{version}

%description -n %{name}+nsanimation
This metapackage enables feature "NSAnimation" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsanimationcontext
Summary:        Bindings to the AppKit framework - feature "NSAnimationContext"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsdate) >= 0.2.2
Provides:       crate(%{pkgname}/nsanimationcontext) = %{version}

%description -n %{name}+nsanimationcontext
This metapackage enables feature "NSAnimationContext" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsappearance
Summary:        Bindings to the AppKit framework - feature "NSAppearance" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsbundle) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nsappearance) = %{version}
Provides:       crate(%{pkgname}/nstabviewcontroller) = %{version}

%description -n %{name}+nsappearance
This metapackage enables feature "NSAppearance" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "NSTabViewController" feature.

%package     -n %{name}+nsapplescriptextensions
Summary:        Bindings to the AppKit framework - feature "NSAppleScriptExtensions"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsapplescript) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsattributedstring) >= 0.2.2
Provides:       crate(%{pkgname}/nsapplescriptextensions) = %{version}

%description -n %{name}+nsapplescriptextensions
This metapackage enables feature "NSAppleScriptExtensions" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsapplication
Summary:        Bindings to the AppKit framework - feature "NSApplication"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdata) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdate) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsexception) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsnotification) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobjcruntime) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsurl) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsuseractivity) >= 0.2.2
Provides:       crate(%{pkgname}/nsapplication) = %{version}

%description -n %{name}+nsapplication
This metapackage enables feature "NSApplication" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsapplicationscripting
Summary:        Bindings to the AppKit framework - feature "NSApplicationScripting" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Provides:       crate(%{pkgname}/nsapplicationscripting) = %{version}
Provides:       crate(%{pkgname}/nspagelayout) = %{version}

%description -n %{name}+nsapplicationscripting
This metapackage enables feature "NSApplicationScripting" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "NSPageLayout" feature.

%package     -n %{name}+nsarraycontroller
Summary:        Bindings to the AppKit framework - feature "NSArrayController"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsindexset) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nspredicate) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nssortdescriptor) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nsarraycontroller) = %{version}

%description -n %{name}+nsarraycontroller
This metapackage enables feature "NSArrayController" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsattributedstring
Summary:        Bindings to the AppKit framework - feature "NSAttributedString"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsattributedstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdata) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsfilewrapper) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsrange) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsurl) >= 0.2.2
Provides:       crate(%{pkgname}/nsattributedstring) = %{version}

%description -n %{name}+nsattributedstring
This metapackage enables feature "NSAttributedString" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsbezierpath
Summary:        Bindings to the AppKit framework - feature "NSBezierPath"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsaffinetransform) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Provides:       crate(%{pkgname}/nsbezierpath) = %{version}

%description -n %{name}+nsbezierpath
This metapackage enables feature "NSBezierPath" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsbitmapimagerep
Summary:        Bindings to the AppKit framework - feature "NSBitmapImageRep"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-core-image-0.2/ciimage) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdata) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nsbitmapimagerep) = %{version}

%description -n %{name}+nsbitmapimagerep
This metapackage enables feature "NSBitmapImageRep" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsbox
Summary:        Bindings to the AppKit framework - feature "NSBox" and 13 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nsbox) = %{version}
Provides:       crate(%{pkgname}/nscombobutton) = %{version}
Provides:       crate(%{pkgname}/nsform) = %{version}
Provides:       crate(%{pkgname}/nslevelindicatorcell) = %{version}
Provides:       crate(%{pkgname}/nsmenuitemcell) = %{version}
Provides:       crate(%{pkgname}/nsscrubberitemview) = %{version}
Provides:       crate(%{pkgname}/nssecuretextfield) = %{version}
Provides:       crate(%{pkgname}/nssegmentedcell) = %{version}
Provides:       crate(%{pkgname}/nsslider) = %{version}
Provides:       crate(%{pkgname}/nsslidercell) = %{version}
Provides:       crate(%{pkgname}/nsslidertouchbaritem) = %{version}
Provides:       crate(%{pkgname}/nsstatusbarbutton) = %{version}
Provides:       crate(%{pkgname}/nstableheadercell) = %{version}
Provides:       crate(%{pkgname}/nstextattachmentcell) = %{version}

%description -n %{name}+nsbox
This metapackage enables feature "NSBox" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "NSComboButton", "NSForm", "NSLevelIndicatorCell", "NSMenuItemCell", "NSScrubberItemView", "NSSecureTextField", "NSSegmentedCell", "NSSlider", "NSSliderCell", "NSSliderTouchBarItem", "NSStatusBarButton", "NSTableHeaderCell", and "NSTextAttachmentCell" features.

%package     -n %{name}+nsbrowser
Summary:        Bindings to the AppKit framework - feature "NSBrowser"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsindexpath) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsindexset) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsnotification) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsurl) >= 0.2.2
Provides:       crate(%{pkgname}/nsbrowser) = %{version}

%description -n %{name}+nsbrowser
This metapackage enables feature "NSBrowser" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsbutton
Summary:        Bindings to the AppKit framework - feature "NSButton"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsattributedstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nsbutton) = %{version}

%description -n %{name}+nsbutton
This metapackage enables feature "NSButton" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsbuttoncell
Summary:        Bindings to the AppKit framework - feature "NSButtonCell" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsattributedstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nsbuttoncell) = %{version}
Provides:       crate(%{pkgname}/nsformcell) = %{version}

%description -n %{name}+nsbuttoncell
This metapackage enables feature "NSButtonCell" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "NSFormCell" feature.

%package     -n %{name}+nsciimagerep
Summary:        Bindings to the AppKit framework - feature "NSCIImageRep"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-core-image-0.2/ciimage) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Provides:       crate(%{pkgname}/nsciimagerep) = %{version}

%description -n %{name}+nsciimagerep
This metapackage enables feature "NSCIImageRep" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nscachedimagerep
Summary:        Bindings to the AppKit framework - feature "NSCachedImageRep" and 16 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Provides:       crate(%{pkgname}/nscachedimagerep) = %{version}
Provides:       crate(%{pkgname}/nscolorwell) = %{version}
Provides:       crate(%{pkgname}/nscursor) = %{version}
Provides:       crate(%{pkgname}/nscustomimagerep) = %{version}
Provides:       crate(%{pkgname}/nsgesturerecognizer) = %{version}
Provides:       crate(%{pkgname}/nsimageview) = %{version}
Provides:       crate(%{pkgname}/nslevelindicator) = %{version}
Provides:       crate(%{pkgname}/nsmagnificationgesturerecognizer) = %{version}
Provides:       crate(%{pkgname}/nspanel) = %{version}
Provides:       crate(%{pkgname}/nspangesturerecognizer) = %{version}
Provides:       crate(%{pkgname}/nsrotationgesturerecognizer) = %{version}
Provides:       crate(%{pkgname}/nsrulermarker) = %{version}
Provides:       crate(%{pkgname}/nsstepper) = %{version}
Provides:       crate(%{pkgname}/nsswitch) = %{version}
Provides:       crate(%{pkgname}/nstableheaderview) = %{version}
Provides:       crate(%{pkgname}/nstablerowview) = %{version}
Provides:       crate(%{pkgname}/nsvisualeffectview) = %{version}

%description -n %{name}+nscachedimagerep
This metapackage enables feature "NSCachedImageRep" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "NSColorWell", "NSCursor", "NSCustomImageRep", "NSGestureRecognizer", "NSImageView", "NSLevelIndicator", "NSMagnificationGestureRecognizer", "NSPanGestureRecognizer", "NSPanel", "NSRotationGestureRecognizer", "NSRulerMarker", "NSStepper", "NSSwitch", "NSTableHeaderView", "NSTableRowView", and "NSVisualEffectView" features.

%package     -n %{name}+nscandidatelisttouchbaritem
Summary:        Bindings to the AppKit framework - feature "NSCandidateListTouchBarItem"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsattributedstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsrange) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nscandidatelisttouchbaritem) = %{version}

%description -n %{name}+nscandidatelisttouchbaritem
This metapackage enables feature "NSCandidateListTouchBarItem" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nscell
Summary:        Bindings to the AppKit framework - feature "NSCell"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsattributedstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsformatter) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsnotification) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobjcruntime) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nscell) = %{version}

%description -n %{name}+nscell
This metapackage enables feature "NSCell" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsclickgesturerecognizer
Summary:        Bindings to the AppKit framework - feature "NSClickGestureRecognizer" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Provides:       crate(%{pkgname}/nsclickgesturerecognizer) = %{version}
Provides:       crate(%{pkgname}/nscontroller) = %{version}
Provides:       crate(%{pkgname}/nsmovie) = %{version}

%description -n %{name}+nsclickgesturerecognizer
This metapackage enables feature "NSClickGestureRecognizer" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "NSController", and "NSMovie" features.

%package     -n %{name}+nsclipview
Summary:        Bindings to the AppKit framework - feature "NSClipView"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsnotification) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Provides:       crate(%{pkgname}/nsclipview) = %{version}

%description -n %{name}+nsclipview
This metapackage enables feature "NSClipView" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nscollectionview
Summary:        Bindings to the AppKit framework - feature "NSCollectionView"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsbundle) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsindexpath) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsindexset) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobjcruntime) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsset) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsurl) >= 0.2.2
Provides:       crate(%{pkgname}/nscollectionview) = %{version}

%description -n %{name}+nscollectionview
This metapackage enables feature "NSCollectionView" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nscollectionviewcompositionallayout
Summary:        Bindings to the AppKit framework - feature "NSCollectionViewCompositionalLayout"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsindexpath) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nscollectionviewcompositionallayout) = %{version}

%description -n %{name}+nscollectionviewcompositionallayout
This metapackage enables feature "NSCollectionViewCompositionalLayout" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nscollectionviewflowlayout
Summary:        Bindings to the AppKit framework - feature "NSCollectionViewFlowLayout"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsindexpath) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nscollectionviewflowlayout) = %{version}

%description -n %{name}+nscollectionviewflowlayout
This metapackage enables feature "NSCollectionViewFlowLayout" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nscollectionviewgridlayout
Summary:        Bindings to the AppKit framework - feature "NSCollectionViewGridLayout"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Provides:       crate(%{pkgname}/nscollectionviewgridlayout) = %{version}

%description -n %{name}+nscollectionviewgridlayout
This metapackage enables feature "NSCollectionViewGridLayout" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nscollectionviewlayout
Summary:        Bindings to the AppKit framework - feature "NSCollectionViewLayout"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsindexpath) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsset) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nscollectionviewlayout) = %{version}

%description -n %{name}+nscollectionviewlayout
This metapackage enables feature "NSCollectionViewLayout" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nscollectionviewtransitionlayout
Summary:        Bindings to the AppKit framework - feature "NSCollectionViewTransitionLayout" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nscollectionviewtransitionlayout) = %{version}
Provides:       crate(%{pkgname}/nssearchtoolbaritem) = %{version}
Provides:       crate(%{pkgname}/nstabviewitem) = %{version}

%description -n %{name}+nscollectionviewtransitionlayout
This metapackage enables feature "NSCollectionViewTransitionLayout" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "NSSearchToolbarItem", and "NSTabViewItem" features.

%package     -n %{name}+nscolor
Summary:        Bindings to the AppKit framework - feature "NSColor"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-core-image-0.2/cicolor) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsbundle) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsnotification) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nscolor) = %{version}

%description -n %{name}+nscolor
This metapackage enables feature "NSColor" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nscolorlist
Summary:        Bindings to the AppKit framework - feature "NSColorList"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsnotification) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsurl) >= 0.2.2
Provides:       crate(%{pkgname}/nscolorlist) = %{version}

%description -n %{name}+nscolorlist
This metapackage enables feature "NSColorList" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nscolorpanel
Summary:        Bindings to the AppKit framework - feature "NSColorPanel"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsnotification) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nscolorpanel) = %{version}

%description -n %{name}+nscolorpanel
This metapackage enables feature "NSColorPanel" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nscolorpickertouchbaritem
Summary:        Bindings to the AppKit framework - feature "NSColorPickerTouchBarItem" and 3 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nscolorpickertouchbaritem) = %{version}
Provides:       crate(%{pkgname}/nspickertouchbaritem) = %{version}
Provides:       crate(%{pkgname}/nssharingservicepickertouchbaritem) = %{version}
Provides:       crate(%{pkgname}/nswindowcontroller) = %{version}

%description -n %{name}+nscolorpickertouchbaritem
This metapackage enables feature "NSColorPickerTouchBarItem" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "NSPickerTouchBarItem", "NSSharingServicePickerTouchBarItem", and "NSWindowController" features.

%package     -n %{name}+nscolorspace
Summary:        Bindings to the AppKit framework - feature "NSColorSpace"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdata) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nscolorspace) = %{version}

%description -n %{name}+nscolorspace
This metapackage enables feature "NSColorSpace" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nscombobox
Summary:        Bindings to the AppKit framework - feature "NSComboBox" and 5 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsnotification) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nscombobox) = %{version}
Provides:       crate(%{pkgname}/nsdrawer) = %{version}
Provides:       crate(%{pkgname}/nsmatrix) = %{version}
Provides:       crate(%{pkgname}/nspopupbutton) = %{version}
Provides:       crate(%{pkgname}/nspopupbuttoncell) = %{version}
Provides:       crate(%{pkgname}/nssplitview) = %{version}

%description -n %{name}+nscombobox
This metapackage enables feature "NSComboBox" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "NSDrawer", "NSMatrix", "NSPopUpButton", "NSPopUpButtonCell", and "NSSplitView" features.

%package     -n %{name}+nscomboboxcell
Summary:        Bindings to the AppKit framework - feature "NSComboBoxCell" and 4 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nscomboboxcell) = %{version}
Provides:       crate(%{pkgname}/nsgrouptouchbaritem) = %{version}
Provides:       crate(%{pkgname}/nssearchfield) = %{version}
Provides:       crate(%{pkgname}/nssearchfieldcell) = %{version}
Provides:       crate(%{pkgname}/nssegmentedcontrol) = %{version}

%description -n %{name}+nscomboboxcell
This metapackage enables feature "NSComboBoxCell" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "NSGroupTouchBarItem", "NSSearchField", "NSSearchFieldCell", and "NSSegmentedControl" features.

%package     -n %{name}+nscontrol
Summary:        Bindings to the AppKit framework - feature "NSControl"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsattributedstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsformatter) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsnotification) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsrange) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nscontrol) = %{version}

%description -n %{name}+nscontrol
This metapackage enables feature "NSControl" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsdataasset
Summary:        Bindings to the AppKit framework - feature "NSDataAsset"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsbundle) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdata) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nsdataasset) = %{version}

%description -n %{name}+nsdataasset
This metapackage enables feature "NSDataAsset" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsdatepicker
Summary:        Bindings to the AppKit framework - feature "NSDatePicker"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nscalendar) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdate) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nslocale) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nstimezone) >= 0.2.2
Provides:       crate(%{pkgname}/nsdatepicker) = %{version}

%description -n %{name}+nsdatepicker
This metapackage enables feature "NSDatePicker" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsdatepickercell
Summary:        Bindings to the AppKit framework - feature "NSDatePickerCell"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.2/nscalendar) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdate) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nslocale) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nstimezone) >= 0.2.2
Provides:       crate(%{pkgname}/nsdatepickercell) = %{version}

%description -n %{name}+nsdatepickercell
This metapackage enables feature "NSDatePickerCell" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsdictionarycontroller
Summary:        Bindings to the AppKit framework - feature "NSDictionaryController"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nsdictionarycontroller) = %{version}

%description -n %{name}+nsdictionarycontroller
This metapackage enables feature "NSDictionaryController" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsdiffabledatasource
Summary:        Bindings to the AppKit framework - feature "NSDiffableDataSource"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsindexpath) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nsdiffabledatasource) = %{version}

%description -n %{name}+nsdiffabledatasource
This metapackage enables feature "NSDiffableDataSource" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsdocument
Summary:        Bindings to the AppKit framework - feature "NSDocument"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdata) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdate) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsfilepresenter) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsfileversion) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsfilewrapper) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsset) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsundomanager) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsurl) >= 0.2.2
Provides:       crate(%{pkgname}/nsdocument) = %{version}

%description -n %{name}+nsdocument
This metapackage enables feature "NSDocument" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsdocumentcontroller
Summary:        Bindings to the AppKit framework - feature "NSDocumentController"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdate) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsurl) >= 0.2.2
Provides:       crate(%{pkgname}/nsdocumentcontroller) = %{version}

%description -n %{name}+nsdocumentcontroller
This metapackage enables feature "NSDocumentController" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsdocumentscripting
Summary:        Bindings to the AppKit framework - feature "NSDocumentScripting"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsscriptcommand) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsscriptobjectspecifiers) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsscriptstandardsuitecommands) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nsdocumentscripting) = %{version}

%description -n %{name}+nsdocumentscripting
This metapackage enables feature "NSDocumentScripting" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsdragging
Summary:        Bindings to the AppKit framework - feature "NSDragging"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobjcruntime) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsurl) >= 0.2.2
Provides:       crate(%{pkgname}/nsdragging) = %{version}

%description -n %{name}+nsdragging
This metapackage enables feature "NSDragging" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsdraggingitem
Summary:        Bindings to the AppKit framework - feature "NSDraggingItem"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nsdraggingitem) = %{version}

%description -n %{name}+nsdraggingitem
This metapackage enables feature "NSDraggingItem" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsdraggingsession
Summary:        Bindings to the AppKit framework - feature "NSDraggingSession"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nsdraggingsession) = %{version}

%description -n %{name}+nsdraggingsession
This metapackage enables feature "NSDraggingSession" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsepsimagerep
Summary:        Bindings to the AppKit framework - feature "NSEPSImageRep" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdata) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Provides:       crate(%{pkgname}/nsepsimagerep) = %{version}
Provides:       crate(%{pkgname}/nspdfimagerep) = %{version}
Provides:       crate(%{pkgname}/nspictimagerep) = %{version}

%description -n %{name}+nsepsimagerep
This metapackage enables feature "NSEPSImageRep" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "NSPDFImageRep", and "NSPICTImageRep" features.

%package     -n %{name}+nserrors
Summary:        Bindings to the AppKit framework - feature "NSErrors"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsobjcruntime) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nserrors) = %{version}

%description -n %{name}+nserrors
This metapackage enables feature "NSErrors" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsevent
Summary:        Bindings to the AppKit framework - feature "NSEvent"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdate) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsset) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nsevent) = %{version}

%description -n %{name}+nsevent
This metapackage enables feature "NSEvent" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsfilepromiseprovider
Summary:        Bindings to the AppKit framework - feature "NSFilePromiseProvider"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsoperation) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsurl) >= 0.2.2
Provides:       crate(%{pkgname}/nsfilepromiseprovider) = %{version}

%description -n %{name}+nsfilepromiseprovider
This metapackage enables feature "NSFilePromiseProvider" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsfilepromisereceiver
Summary:        Bindings to the AppKit framework - feature "NSFilePromiseReceiver"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsoperation) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsurl) >= 0.2.2
Provides:       crate(%{pkgname}/nsfilepromisereceiver) = %{version}

%description -n %{name}+nsfilepromisereceiver
This metapackage enables feature "NSFilePromiseReceiver" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsfilewrapperextensions
Summary:        Bindings to the AppKit framework - feature "NSFileWrapperExtensions"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsfilewrapper) >= 0.2.2
Provides:       crate(%{pkgname}/nsfilewrapperextensions) = %{version}

%description -n %{name}+nsfilewrapperextensions
This metapackage enables feature "NSFileWrapperExtensions" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsfont
Summary:        Bindings to the AppKit framework - feature "NSFont"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsaffinetransform) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscharacterset) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsnotification) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nsfont) = %{version}

%description -n %{name}+nsfont
This metapackage enables feature "NSFont" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsfontassetrequest
Summary:        Bindings to the AppKit framework - feature "NSFontAssetRequest"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsprogress) >= 0.2.2
Provides:       crate(%{pkgname}/nsfontassetrequest) = %{version}

%description -n %{name}+nsfontassetrequest
This metapackage enables feature "NSFontAssetRequest" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsfontcollection
Summary:        Bindings to the AppKit framework - feature "NSFontCollection"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nslocale) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsnotification) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsvalue) >= 0.2.2
Provides:       crate(%{pkgname}/nsfontcollection) = %{version}

%description -n %{name}+nsfontcollection
This metapackage enables feature "NSFontCollection" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsfontdescriptor
Summary:        Bindings to the AppKit framework - feature "NSFontDescriptor"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.2/nsaffinetransform) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsset) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nsfontdescriptor) = %{version}

%description -n %{name}+nsfontdescriptor
This metapackage enables feature "NSFontDescriptor" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsfontmanager
Summary:        Bindings to the AppKit framework - feature "NSFontManager" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nsfontmanager) = %{version}
Provides:       crate(%{pkgname}/nslayoutconstraint) = %{version}

%description -n %{name}+nsfontmanager
This metapackage enables feature "NSFontManager" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "NSLayoutConstraint" feature.

%package     -n %{name}+nsfontpanel
Summary:        Bindings to the AppKit framework - feature "NSFontPanel" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Provides:       crate(%{pkgname}/nsfontpanel) = %{version}
Provides:       crate(%{pkgname}/nstextinsertionindicator) = %{version}

%description -n %{name}+nsfontpanel
This metapackage enables feature "NSFontPanel" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "NSTextInsertionIndicator" feature.

%package     -n %{name}+nsglyphgenerator
Summary:        Bindings to the AppKit framework - feature "NSGlyphGenerator"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsattributedstring) >= 0.2.2
Provides:       crate(%{pkgname}/nsglyphgenerator) = %{version}

%description -n %{name}+nsglyphgenerator
This metapackage enables feature "NSGlyphGenerator" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsglyphinfo
Summary:        Bindings to the AppKit framework - feature "NSGlyphInfo" and 4 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nsglyphinfo) = %{version}
Provides:       crate(%{pkgname}/nsmenuitembadge) = %{version}
Provides:       crate(%{pkgname}/nsmenutoolbaritem) = %{version}
Provides:       crate(%{pkgname}/nstableviewrowaction) = %{version}
Provides:       crate(%{pkgname}/nstrackingseparatortoolbaritem) = %{version}

%description -n %{name}+nsglyphinfo
This metapackage enables feature "NSGlyphInfo" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "NSMenuItemBadge", "NSMenuToolbarItem", "NSTableViewRowAction", and "NSTrackingSeparatorToolbarItem" features.

%package     -n %{name}+nsgradient
Summary:        Bindings to the AppKit framework - feature "NSGradient"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Provides:       crate(%{pkgname}/nsgradient) = %{version}

%description -n %{name}+nsgradient
This metapackage enables feature "NSGradient" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsgraphicscontext
Summary:        Bindings to the AppKit framework - feature "NSGraphicsContext"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-core-image-0.2/cicontext) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nsgraphicscontext) = %{version}

%description -n %{name}+nsgraphicscontext
This metapackage enables feature "NSGraphicsContext" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsgridview
Summary:        Bindings to the AppKit framework - feature "NSGridView"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsrange) >= 0.2.2
Provides:       crate(%{pkgname}/nsgridview) = %{version}

%description -n %{name}+nsgridview
This metapackage enables feature "NSGridView" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nshelpmanager
Summary:        Bindings to the AppKit framework - feature "NSHelpManager"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsattributedstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsbundle) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsnotification) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nshelpmanager) = %{version}

%description -n %{name}+nshelpmanager
This metapackage enables feature "NSHelpManager" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsimage
Summary:        Bindings to the AppKit framework - feature "NSImage"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsbundle) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdata) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsitemprovider) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nslocale) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsurl) >= 0.2.2
Provides:       crate(%{pkgname}/nsimage) = %{version}

%description -n %{name}+nsimage
This metapackage enables feature "NSImage" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsimagerep
Summary:        Bindings to the AppKit framework - feature "NSImageRep"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdata) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsnotification) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsurl) >= 0.2.2
Provides:       crate(%{pkgname}/nsimagerep) = %{version}

%description -n %{name}+nsimagerep
This metapackage enables feature "NSImageRep" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsinputmanager
Summary:        Bindings to the AppKit framework - feature "NSInputManager" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsattributedstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsrange) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nsinputmanager) = %{version}
Provides:       crate(%{pkgname}/nstextinputclient) = %{version}

%description -n %{name}+nsinputmanager
This metapackage enables feature "NSInputManager" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "NSTextInputClient" feature.

%package     -n %{name}+nsinputserver
Summary:        Bindings to the AppKit framework - feature "NSInputServer"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsrange) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nsinputserver) = %{version}

%description -n %{name}+nsinputserver
This metapackage enables feature "NSInputServer" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsitemprovider
Summary:        Bindings to the AppKit framework - feature "NSItemProvider"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsitemprovider) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nsitemprovider) = %{version}

%description -n %{name}+nsitemprovider
This metapackage enables feature "NSItemProvider" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nskeyvaluebinding
Summary:        Bindings to the AppKit framework - feature "NSKeyValueBinding"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-core-data-0.2/nsattributedescription) >= 0.2.2
Requires:       crate(objc2-core-data-0.2/nspropertydescription) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nskeyvaluebinding) = %{version}

%description -n %{name}+nskeyvaluebinding
This metapackage enables feature "NSKeyValueBinding" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nslayoutanchor
Summary:        Bindings to the AppKit framework - feature "NSLayoutAnchor" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nslayoutanchor) = %{version}
Provides:       crate(%{pkgname}/nslayoutguide) = %{version}

%description -n %{name}+nslayoutanchor
This metapackage enables feature "NSLayoutAnchor" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "NSLayoutGuide" feature.

%package     -n %{name}+nslayoutmanager
Summary:        Bindings to the AppKit framework - feature "NSLayoutManager"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsattributedstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsrange) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nslayoutmanager) = %{version}

%description -n %{name}+nslayoutmanager
This metapackage enables feature "NSLayoutManager" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsmedialibrarybrowsercontroller
Summary:        Bindings to the AppKit framework - feature "NSMediaLibraryBrowserController"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Provides:       crate(%{pkgname}/nsmedialibrarybrowsercontroller) = %{version}

%description -n %{name}+nsmedialibrarybrowsercontroller
This metapackage enables feature "NSMediaLibraryBrowserController" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsmenu
Summary:        Bindings to the AppKit framework - feature "NSMenu"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsnotification) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nszone) >= 0.2.2
Provides:       crate(%{pkgname}/nsmenu) = %{version}

%description -n %{name}+nsmenu
This metapackage enables feature "NSMenu" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsmenuitem
Summary:        Bindings to the AppKit framework - feature "NSMenuItem"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsattributedstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nsmenuitem) = %{version}

%description -n %{name}+nsmenuitem
This metapackage enables feature "NSMenuItem" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsnib
Summary:        Bindings to the AppKit framework - feature "NSNib"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsbundle) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdata) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsurl) >= 0.2.2
Provides:       crate(%{pkgname}/nsnib) = %{version}

%description -n %{name}+nsnib
This metapackage enables feature "NSNib" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsobjectcontroller
Summary:        Bindings to the AppKit framework - feature "NSObjectController"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-core-data-0.2/nsfetchrequest) >= 0.2.2
Requires:       crate(objc2-core-data-0.2/nsmanagedobjectcontext) >= 0.2.2
Requires:       crate(objc2-core-data-0.2/nspersistentstorerequest) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nspredicate) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nsobjectcontroller) = %{version}

%description -n %{name}+nsobjectcontroller
This metapackage enables feature "NSObjectController" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsopenpanel
Summary:        Bindings to the AppKit framework - feature "NSOpenPanel"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsurl) >= 0.2.2
Provides:       crate(%{pkgname}/nsopenpanel) = %{version}

%description -n %{name}+nsopenpanel
This metapackage enables feature "NSOpenPanel" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsoutlineview
Summary:        Bindings to the AppKit framework - feature "NSOutlineView"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsindexset) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsnotification) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nssortdescriptor) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsurl) >= 0.2.2
Provides:       crate(%{pkgname}/nsoutlineview) = %{version}

%description -n %{name}+nsoutlineview
This metapackage enables feature "NSOutlineView" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nspdfinfo
Summary:        Bindings to the AppKit framework - feature "NSPDFInfo"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsurl) >= 0.2.2
Provides:       crate(%{pkgname}/nspdfinfo) = %{version}

%description -n %{name}+nspdfinfo
This metapackage enables feature "NSPDFInfo" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nspdfpanel
Summary:        Bindings to the AppKit framework - feature "NSPDFPanel"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nspdfpanel) = %{version}

%description -n %{name}+nspdfpanel
This metapackage enables feature "NSPDFPanel" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nspagecontroller
Summary:        Bindings to the AppKit framework - feature "NSPageController" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsbundle) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nspagecontroller) = %{version}
Provides:       crate(%{pkgname}/nssplitviewcontroller) = %{version}

%description -n %{name}+nspagecontroller
This metapackage enables feature "NSPageController" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "NSSplitViewController" feature.

%package     -n %{name}+nsparagraphstyle
Summary:        Bindings to the AppKit framework - feature "NSParagraphStyle"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscharacterset) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nslocale) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nsparagraphstyle) = %{version}

%description -n %{name}+nsparagraphstyle
This metapackage enables feature "NSParagraphStyle" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nspasteboard
Summary:        Bindings to the AppKit framework - feature "NSPasteboard"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdata) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsfilewrapper) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsurl) >= 0.2.2
Provides:       crate(%{pkgname}/nspasteboard) = %{version}

%description -n %{name}+nspasteboard
This metapackage enables feature "NSPasteboard" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nspasteboarditem
Summary:        Bindings to the AppKit framework - feature "NSPasteboardItem"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdata) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nspasteboarditem) = %{version}

%description -n %{name}+nspasteboarditem
This metapackage enables feature "NSPasteboardItem" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nspathcell
Summary:        Bindings to the AppKit framework - feature "NSPathCell" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsattributedstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsurl) >= 0.2.2
Provides:       crate(%{pkgname}/nspathcell) = %{version}
Provides:       crate(%{pkgname}/nspathcontrol) = %{version}

%description -n %{name}+nspathcell
This metapackage enables feature "NSPathCell" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "NSPathControl" feature.

%package     -n %{name}+nspathcomponentcell
Summary:        Bindings to the AppKit framework - feature "NSPathComponentCell"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsurl) >= 0.2.2
Provides:       crate(%{pkgname}/nspathcomponentcell) = %{version}

%description -n %{name}+nspathcomponentcell
This metapackage enables feature "NSPathComponentCell" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nspathcontrolitem
Summary:        Bindings to the AppKit framework - feature "NSPathControlItem"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsattributedstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsurl) >= 0.2.2
Provides:       crate(%{pkgname}/nspathcontrolitem) = %{version}

%description -n %{name}+nspathcontrolitem
This metapackage enables feature "NSPathControlItem" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nspersistentdocument
Summary:        Bindings to the AppKit framework - feature "NSPersistentDocument"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-core-data-0.2/nsmanagedobjectcontext) >= 0.2.2
Requires:       crate(objc2-core-data-0.2/nsmanagedobjectmodel) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsfilepresenter) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsurl) >= 0.2.2
Provides:       crate(%{pkgname}/nspersistentdocument) = %{version}

%description -n %{name}+nspersistentdocument
This metapackage enables feature "NSPersistentDocument" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nspopover
Summary:        Bindings to the AppKit framework - feature "NSPopover" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsnotification) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nspopover) = %{version}
Provides:       crate(%{pkgname}/nsscroller) = %{version}
Provides:       crate(%{pkgname}/nsscrollview) = %{version}

%description -n %{name}+nspopover
This metapackage enables feature "NSPopover" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "NSScrollView", and "NSScroller" features.

%package     -n %{name}+nspredicateeditor
Summary:        Bindings to the AppKit framework - feature "NSPredicateEditor" and 4 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Provides:       crate(%{pkgname}/nspredicateeditor) = %{version}
Provides:       crate(%{pkgname}/nsstackview) = %{version}
Provides:       crate(%{pkgname}/nstablecellview) = %{version}
Provides:       crate(%{pkgname}/nstabview) = %{version}
Provides:       crate(%{pkgname}/nstextcontainer) = %{version}

%description -n %{name}+nspredicateeditor
This metapackage enables feature "NSPredicateEditor" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "NSStackView", "NSTabView", "NSTableCellView", and "NSTextContainer" features.

%package     -n %{name}+nspredicateeditorrowtemplate
Summary:        Bindings to the AppKit framework - feature "NSPredicateEditorRowTemplate"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-core-data-0.2/nsattributedescription) >= 0.2.2
Requires:       crate(objc2-core-data-0.2/nsentitydescription) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscomparisonpredicate) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsexpression) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nspredicate) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsvalue) >= 0.2.2
Provides:       crate(%{pkgname}/nspredicateeditorrowtemplate) = %{version}

%description -n %{name}+nspredicateeditorrowtemplate
This metapackage enables feature "NSPredicateEditorRowTemplate" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nspressgesturerecognizer
Summary:        Bindings to the AppKit framework - feature "NSPressGestureRecognizer"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdate) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Provides:       crate(%{pkgname}/nspressgesturerecognizer) = %{version}

%description -n %{name}+nspressgesturerecognizer
This metapackage enables feature "NSPressGestureRecognizer" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nspreviewrepresentingactivityitem
Summary:        Bindings to the AppKit framework - feature "NSPreviewRepresentingActivityItem"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsitemprovider) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nspreviewrepresentingactivityitem) = %{version}

%description -n %{name}+nspreviewrepresentingactivityitem
This metapackage enables feature "NSPreviewRepresentingActivityItem" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsprintinfo
Summary:        Bindings to the AppKit framework - feature "NSPrintInfo"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nsprintinfo) = %{version}

%description -n %{name}+nsprintinfo
This metapackage enables feature "NSPrintInfo" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsprintoperation
Summary:        Bindings to the AppKit framework - feature "NSPrintOperation"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsdata) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobjcruntime) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsrange) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nsprintoperation) = %{version}

%description -n %{name}+nsprintoperation
This metapackage enables feature "NSPrintOperation" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsprintpanel
Summary:        Bindings to the AppKit framework - feature "NSPrintPanel"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsset) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nsprintpanel) = %{version}

%description -n %{name}+nsprintpanel
This metapackage enables feature "NSPrintPanel" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsprinter
Summary:        Bindings to the AppKit framework - feature "NSPrinter"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nsprinter) = %{version}

%description -n %{name}+nsprinter
This metapackage enables feature "NSPrinter" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsprogressindicator
Summary:        Bindings to the AppKit framework - feature "NSProgressIndicator"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdate) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsprogress) >= 0.2.2
Provides:       crate(%{pkgname}/nsprogressindicator) = %{version}

%description -n %{name}+nsprogressindicator
This metapackage enables feature "NSProgressIndicator" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsresponder
Summary:        Bindings to the AppKit framework - feature "NSResponder"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsundomanager) >= 0.2.2
Provides:       crate(%{pkgname}/nsresponder) = %{version}

%description -n %{name}+nsresponder
This metapackage enables feature "NSResponder" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsruleeditor
Summary:        Bindings to the AppKit framework - feature "NSRuleEditor"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsindexset) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsnotification) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nspredicate) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nsruleeditor) = %{version}

%description -n %{name}+nsruleeditor
This metapackage enables feature "NSRuleEditor" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsrulerview
Summary:        Bindings to the AppKit framework - feature "NSRulerView"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsvalue) >= 0.2.2
Provides:       crate(%{pkgname}/nsrulerview) = %{version}

%description -n %{name}+nsrulerview
This metapackage enables feature "NSRulerView" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsrunningapplication
Summary:        Bindings to the AppKit framework - feature "NSRunningApplication"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdate) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsurl) >= 0.2.2
Provides:       crate(%{pkgname}/nsrunningapplication) = %{version}

%description -n %{name}+nsrunningapplication
This metapackage enables feature "NSRunningApplication" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nssavepanel
Summary:        Bindings to the AppKit framework - feature "NSSavePanel"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsurl) >= 0.2.2
Provides:       crate(%{pkgname}/nssavepanel) = %{version}

%description -n %{name}+nssavepanel
This metapackage enables feature "NSSavePanel" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsscreen
Summary:        Bindings to the AppKit framework - feature "NSScreen"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdate) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsnotification) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nsscreen) = %{version}

%description -n %{name}+nsscreen
This metapackage enables feature "NSScreen" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsscrubber
Summary:        Bindings to the AppKit framework - feature "NSScrubber"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsindexset) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsrange) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nsscrubber) = %{version}

%description -n %{name}+nsscrubber
This metapackage enables feature "NSScrubber" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsscrubberlayout
Summary:        Bindings to the AppKit framework - feature "NSScrubberLayout"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsindexset) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsset) >= 0.2.2
Provides:       crate(%{pkgname}/nsscrubberlayout) = %{version}

%description -n %{name}+nsscrubberlayout
This metapackage enables feature "NSScrubberLayout" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsshadow
Summary:        Bindings to the AppKit framework - feature "NSShadow" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Provides:       crate(%{pkgname}/nsshadow) = %{version}
Provides:       crate(%{pkgname}/nssplitviewitem) = %{version}

%description -n %{name}+nsshadow
This metapackage enables feature "NSShadow" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "NSSplitViewItem" feature.

%package     -n %{name}+nssharingservice
Summary:        Bindings to the AppKit framework - feature "NSSharingService"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsitemprovider) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsurl) >= 0.2.2
Provides:       crate(%{pkgname}/nssharingservice) = %{version}

%description -n %{name}+nssharingservice
This metapackage enables feature "NSSharingService" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nssharingservicepickertoolbaritem
Summary:        Bindings to the AppKit framework - feature "NSSharingServicePickerToolbarItem" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nssharingservicepickertoolbaritem) = %{version}
Provides:       crate(%{pkgname}/nstoolbaritemgroup) = %{version}

%description -n %{name}+nssharingservicepickertoolbaritem
This metapackage enables feature "NSSharingServicePickerToolbarItem" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "NSToolbarItemGroup" feature.

%package     -n %{name}+nsslideraccessory
Summary:        Bindings to the AppKit framework - feature "NSSliderAccessory" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Provides:       crate(%{pkgname}/nsslideraccessory) = %{version}
Provides:       crate(%{pkgname}/nstintconfiguration) = %{version}

%description -n %{name}+nsslideraccessory
This metapackage enables feature "NSSliderAccessory" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "NSTintConfiguration" feature.

%package     -n %{name}+nssound
Summary:        Bindings to the AppKit framework - feature "NSSound"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsbundle) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdata) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdate) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsurl) >= 0.2.2
Provides:       crate(%{pkgname}/nssound) = %{version}

%description -n %{name}+nssound
This metapackage enables feature "NSSound" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsspeechrecognizer
Summary:        Bindings to the AppKit framework - feature "NSSpeechRecognizer" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nsspeechrecognizer) = %{version}
Provides:       crate(%{pkgname}/nswindowtabgroup) = %{version}

%description -n %{name}+nsspeechrecognizer
This metapackage enables feature "NSSpeechRecognizer" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "NSWindowTabGroup" feature.

%package     -n %{name}+nsspeechsynthesizer
Summary:        Bindings to the AppKit framework - feature "NSSpeechSynthesizer"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsrange) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsurl) >= 0.2.2
Provides:       crate(%{pkgname}/nsspeechsynthesizer) = %{version}

%description -n %{name}+nsspeechsynthesizer
This metapackage enables feature "NSSpeechSynthesizer" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsspellchecker
Summary:        Bindings to the AppKit framework - feature "NSSpellChecker"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsnotification) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsorthography) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsrange) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nstextcheckingresult) >= 0.2.2
Provides:       crate(%{pkgname}/nsspellchecker) = %{version}

%description -n %{name}+nsspellchecker
This metapackage enables feature "NSSpellChecker" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsstatusbar
Summary:        Bindings to the AppKit framework - feature "NSStatusBar" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Provides:       crate(%{pkgname}/nsstatusbar) = %{version}
Provides:       crate(%{pkgname}/nstextviewportlayoutcontroller) = %{version}

%description -n %{name}+nsstatusbar
This metapackage enables feature "NSStatusBar" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "NSTextViewportLayoutController" feature.

%package     -n %{name}+nsstatusitem
Summary:        Bindings to the AppKit framework - feature "NSStatusItem"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.2/nsattributedstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nsstatusitem) = %{version}

%description -n %{name}+nsstatusitem
This metapackage enables feature "NSStatusItem" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nssteppertouchbaritem
Summary:        Bindings to the AppKit framework - feature "NSStepperTouchBarItem"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsformatter) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nssteppertouchbaritem) = %{version}

%description -n %{name}+nssteppertouchbaritem
This metapackage enables feature "NSStepperTouchBarItem" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsstoryboard
Summary:        Bindings to the AppKit framework - feature "NSStoryboard"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsbundle) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nsstoryboard) = %{version}

%description -n %{name}+nsstoryboard
This metapackage enables feature "NSStoryboard" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsstringdrawing
Summary:        Bindings to the AppKit framework - feature "NSStringDrawing"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.2/nsattributedstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nsstringdrawing) = %{version}

%description -n %{name}+nsstringdrawing
This metapackage enables feature "NSStringDrawing" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nstablecolumn
Summary:        Bindings to the AppKit framework - feature "NSTableColumn"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nssortdescriptor) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nstablecolumn) = %{version}

%description -n %{name}+nstablecolumn
This metapackage enables feature "NSTableColumn" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nstableview
Summary:        Bindings to the AppKit framework - feature "NSTableView"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsenumerator) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsindexset) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsnotification) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsrange) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nssortdescriptor) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsurl) >= 0.2.2
Provides:       crate(%{pkgname}/nstableview) = %{version}

%description -n %{name}+nstableview
This metapackage enables feature "NSTableView" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nstext
Summary:        Bindings to the AppKit framework - feature "NSText"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdata) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsnotification) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsrange) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nstext) = %{version}

%description -n %{name}+nstext
This metapackage enables feature "NSText" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nstextalternatives
Summary:        Bindings to the AppKit framework - feature "NSTextAlternatives"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsnotification) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nstextalternatives) = %{version}

%description -n %{name}+nstextalternatives
This metapackage enables feature "NSTextAlternatives" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nstextattachment
Summary:        Bindings to the AppKit framework - feature "NSTextAttachment"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsattributedstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdata) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsfilewrapper) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nstextattachment) = %{version}

%description -n %{name}+nstextattachment
This metapackage enables feature "NSTextAttachment" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nstextcheckingclient
Summary:        Bindings to the AppKit framework - feature "NSTextCheckingClient"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsattributedstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsrange) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nstextcheckingclient) = %{version}

%description -n %{name}+nstextcheckingclient
This metapackage enables feature "NSTextCheckingClient" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nstextcheckingcontroller
Summary:        Bindings to the AppKit framework - feature "NSTextCheckingController"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsattributedstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsrange) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nstextcheckingresult) >= 0.2.2
Provides:       crate(%{pkgname}/nstextcheckingcontroller) = %{version}

%description -n %{name}+nstextcheckingcontroller
This metapackage enables feature "NSTextCheckingController" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nstextcontentmanager
Summary:        Bindings to the AppKit framework - feature "NSTextContentManager"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsattributedstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsnotification) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsrange) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nstextcontentmanager) = %{version}

%description -n %{name}+nstextcontentmanager
This metapackage enables feature "NSTextContentManager" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nstextelement
Summary:        Bindings to the AppKit framework - feature "NSTextElement" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsattributedstring) >= 0.2.2
Provides:       crate(%{pkgname}/nstextelement) = %{version}
Provides:       crate(%{pkgname}/nstextstoragescripting) = %{version}

%description -n %{name}+nstextelement
This metapackage enables feature "NSTextElement" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "NSTextStorageScripting" feature.

%package     -n %{name}+nstextfield
Summary:        Bindings to the AppKit framework - feature "NSTextField"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsattributedstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsnotification) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsrange) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nstextcheckingresult) >= 0.2.2
Provides:       crate(%{pkgname}/nstextfield) = %{version}

%description -n %{name}+nstextfield
This metapackage enables feature "NSTextField" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nstextfieldcell
Summary:        Bindings to the AppKit framework - feature "NSTextFieldCell"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsattributedstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nstextfieldcell) = %{version}

%description -n %{name}+nstextfieldcell
This metapackage enables feature "NSTextFieldCell" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nstextfinder
Summary:        Bindings to the AppKit framework - feature "NSTextFinder"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsrange) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsvalue) >= 0.2.2
Provides:       crate(%{pkgname}/nstextfinder) = %{version}

%description -n %{name}+nstextfinder
This metapackage enables feature "NSTextFinder" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nstextinputcontext
Summary:        Bindings to the AppKit framework - feature "NSTextInputContext"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsnotification) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nstextinputcontext) = %{version}

%description -n %{name}+nstextinputcontext
This metapackage enables feature "NSTextInputContext" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nstextlayoutfragment
Summary:        Bindings to the AppKit framework - feature "NSTextLayoutFragment"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsoperation) >= 0.2.2
Provides:       crate(%{pkgname}/nstextlayoutfragment) = %{version}

%description -n %{name}+nstextlayoutfragment
This metapackage enables feature "NSTextLayoutFragment" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nstextlayoutmanager
Summary:        Bindings to the AppKit framework - feature "NSTextLayoutManager"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsattributedstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsoperation) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nstextlayoutmanager) = %{version}

%description -n %{name}+nstextlayoutmanager
This metapackage enables feature "NSTextLayoutManager" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nstextlinefragment
Summary:        Bindings to the AppKit framework - feature "NSTextLineFragment"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsattributedstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsrange) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nstextlinefragment) = %{version}

%description -n %{name}+nstextlinefragment
This metapackage enables feature "NSTextLineFragment" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nstextlist
Summary:        Bindings to the AppKit framework - feature "NSTextList"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nstextlist) = %{version}

%description -n %{name}+nstextlist
This metapackage enables feature "NSTextList" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nstextlistelement
Summary:        Bindings to the AppKit framework - feature "NSTextListElement"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsattributedstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nstextlistelement) = %{version}

%description -n %{name}+nstextlistelement
This metapackage enables feature "NSTextListElement" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nstextrange
Summary:        Bindings to the AppKit framework - feature "NSTextRange"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsobjcruntime) >= 0.2.2
Provides:       crate(%{pkgname}/nstextrange) = %{version}

%description -n %{name}+nstextrange
This metapackage enables feature "NSTextRange" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nstextselection
Summary:        Bindings to the AppKit framework - feature "NSTextSelection"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsattributedstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nstextselection) = %{version}

%description -n %{name}+nstextselection
This metapackage enables feature "NSTextSelection" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nstextselectionnavigation
Summary:        Bindings to the AppKit framework - feature "NSTextSelectionNavigation"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nstextselectionnavigation) = %{version}

%description -n %{name}+nstextselectionnavigation
This metapackage enables feature "NSTextSelectionNavigation" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nstextstorage
Summary:        Bindings to the AppKit framework - feature "NSTextStorage"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsattributedstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsnotification) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsrange) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nstextstorage) = %{version}

%description -n %{name}+nstextstorage
This metapackage enables feature "NSTextStorage" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nstexttable
Summary:        Bindings to the AppKit framework - feature "NSTextTable"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsrange) >= 0.2.2
Provides:       crate(%{pkgname}/nstexttable) = %{version}

%description -n %{name}+nstexttable
This metapackage enables feature "NSTextTable" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nstextview
Summary:        Bindings to the AppKit framework - feature "NSTextView"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsattributedstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsnotification) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsorthography) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsrange) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nstextcheckingresult) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsundomanager) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsurl) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsvalue) >= 0.2.2
Provides:       crate(%{pkgname}/nstextview) = %{version}

%description -n %{name}+nstextview
This metapackage enables feature "NSTextView" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nstitlebaraccessoryviewcontroller
Summary:        Bindings to the AppKit framework - feature "NSTitlebarAccessoryViewController"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsbundle) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nstitlebaraccessoryviewcontroller) = %{version}

%description -n %{name}+nstitlebaraccessoryviewcontroller
This metapackage enables feature "NSTitlebarAccessoryViewController" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nstokenfield
Summary:        Bindings to the AppKit framework - feature "NSTokenField"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscharacterset) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdate) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nstokenfield) = %{version}

%description -n %{name}+nstokenfield
This metapackage enables feature "NSTokenField" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nstokenfieldcell
Summary:        Bindings to the AppKit framework - feature "NSTokenFieldCell"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscharacterset) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdate) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nstokenfieldcell) = %{version}

%description -n %{name}+nstokenfieldcell
This metapackage enables feature "NSTokenFieldCell" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nstoolbar
Summary:        Bindings to the AppKit framework - feature "NSToolbar"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsnotification) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsset) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nstoolbar) = %{version}

%description -n %{name}+nstoolbar
This metapackage enables feature "NSToolbar" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nstoolbaritem
Summary:        Bindings to the AppKit framework - feature "NSToolbarItem"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsset) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nstoolbaritem) = %{version}

%description -n %{name}+nstoolbaritem
This metapackage enables feature "NSToolbarItem" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nstouch
Summary:        Bindings to the AppKit framework - feature "NSTouch"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Provides:       crate(%{pkgname}/nstouch) = %{version}

%description -n %{name}+nstouch
This metapackage enables feature "NSTouch" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nstouchbar
Summary:        Bindings to the AppKit framework - feature "NSTouchBar"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsset) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nstouchbar) = %{version}

%description -n %{name}+nstouchbar
This metapackage enables feature "NSTouchBar" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nstrackingarea
Summary:        Bindings to the AppKit framework - feature "NSTrackingArea"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Provides:       crate(%{pkgname}/nstrackingarea) = %{version}

%description -n %{name}+nstrackingarea
This metapackage enables feature "NSTrackingArea" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nstreecontroller
Summary:        Bindings to the AppKit framework - feature "NSTreeController"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsindexpath) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nssortdescriptor) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nstreecontroller) = %{version}

%description -n %{name}+nstreecontroller
This metapackage enables feature "NSTreeController" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nstreenode
Summary:        Bindings to the AppKit framework - feature "NSTreeNode"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsindexpath) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nssortdescriptor) >= 0.2.2
Provides:       crate(%{pkgname}/nstreenode) = %{version}

%description -n %{name}+nstreenode
This metapackage enables feature "NSTreeNode" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nstypesetter
Summary:        Bindings to the AppKit framework - feature "NSTypesetter"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsattributedstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsrange) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nstypesetter) = %{version}

%description -n %{name}+nstypesetter
This metapackage enables feature "NSTypesetter" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsuseractivity
Summary:        Bindings to the AppKit framework - feature "NSUserActivity"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsuseractivity) >= 0.2.2
Provides:       crate(%{pkgname}/nsuseractivity) = %{version}

%description -n %{name}+nsuseractivity
This metapackage enables feature "NSUserActivity" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsuserdefaultscontroller
Summary:        Bindings to the AppKit framework - feature "NSUserDefaultsController"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsuserdefaults) >= 0.2.2
Provides:       crate(%{pkgname}/nsuserdefaultscontroller) = %{version}

%description -n %{name}+nsuserdefaultscontroller
This metapackage enables feature "NSUserDefaultsController" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsuserinterfacecompression
Summary:        Bindings to the AppKit framework - feature "NSUserInterfaceCompression"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsset) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nsuserinterfacecompression) = %{version}

%description -n %{name}+nsuserinterfacecompression
This metapackage enables feature "NSUserInterfaceCompression" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsuserinterfaceitemsearching
Summary:        Bindings to the AppKit framework - feature "NSUserInterfaceItemSearching"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsrange) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nsuserinterfaceitemsearching) = %{version}

%description -n %{name}+nsuserinterfaceitemsearching
This metapackage enables feature "NSUserInterfaceItemSearching" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsview
Summary:        Bindings to the AppKit framework - feature "NSView"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsattributedstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdata) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsnotification) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobjcruntime) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsrange) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-quartz-core-0.2/calayer) >= 0.2.2
Provides:       crate(%{pkgname}/nsview) = %{version}

%description -n %{name}+nsview
This metapackage enables feature "NSView" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsviewcontroller
Summary:        Bindings to the AppKit framework - feature "NSViewController"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsbundle) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsextensioncontext) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsextensionrequesthandling) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nsviewcontroller) = %{version}

%description -n %{name}+nsviewcontroller
This metapackage enables feature "NSViewController" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nswindow
Summary:        Bindings to the AppKit framework - feature "NSWindow"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdata) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdate) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsnotification) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobjcruntime) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsundomanager) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsurl) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsvalue) >= 0.2.2
Provides:       crate(%{pkgname}/nswindow) = %{version}

%description -n %{name}+nswindow
This metapackage enables feature "NSWindow" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nswindowrestoration
Summary:        Bindings to the AppKit framework - feature "NSWindowRestoration"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsnotification) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsoperation) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nswindowrestoration) = %{version}

%description -n %{name}+nswindowrestoration
This metapackage enables feature "NSWindowRestoration" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nswindowscripting
Summary:        Bindings to the AppKit framework - feature "NSWindowScripting"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsscriptcommand) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsscriptstandardsuitecommands) >= 0.2.2
Provides:       crate(%{pkgname}/nswindowscripting) = %{version}

%description -n %{name}+nswindowscripting
This metapackage enables feature "NSWindowScripting" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nswindowtab
Summary:        Bindings to the AppKit framework - feature "NSWindowTab"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsattributedstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nswindowtab) = %{version}

%description -n %{name}+nswindowtab
This metapackage enables feature "NSWindowTab" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsworkspace
Summary:        Bindings to the AppKit framework - feature "NSWorkspace"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.2/nsappleeventdescriptor) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsfilemanager) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsgeometry) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsnotification) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsurl) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsvalue) >= 0.2.2
Provides:       crate(%{pkgname}/nsworkspace) = %{version}

%description -n %{name}+nsworkspace
This metapackage enables feature "NSWorkspace" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+all
Summary:        Bindings to the AppKit framework - feature "all"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/appkitdefines) = %{version}
Requires:       crate(%{pkgname}/appkiterrors) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(%{pkgname}/block2) = %{version}
Requires:       crate(%{pkgname}/libc) = %{version}
Requires:       crate(%{pkgname}/nsaccessibility) = %{version}
Requires:       crate(%{pkgname}/nsaccessibilitycolor) = %{version}
Requires:       crate(%{pkgname}/nsaccessibilityconstants) = %{version}
Requires:       crate(%{pkgname}/nsaccessibilitycustomaction) = %{version}
Requires:       crate(%{pkgname}/nsaccessibilitycustomrotor) = %{version}
Requires:       crate(%{pkgname}/nsaccessibilityelement) = %{version}
Requires:       crate(%{pkgname}/nsaccessibilityprotocols) = %{version}
Requires:       crate(%{pkgname}/nsactioncell) = %{version}
Requires:       crate(%{pkgname}/nsaffinetransform) = %{version}
Requires:       crate(%{pkgname}/nsalert) = %{version}
Requires:       crate(%{pkgname}/nsalignmentfeedbackfilter) = %{version}
Requires:       crate(%{pkgname}/nsanimation) = %{version}
Requires:       crate(%{pkgname}/nsanimationcontext) = %{version}
Requires:       crate(%{pkgname}/nsappearance) = %{version}
Requires:       crate(%{pkgname}/nsapplescriptextensions) = %{version}
Requires:       crate(%{pkgname}/nsapplication) = %{version}
Requires:       crate(%{pkgname}/nsapplicationscripting) = %{version}
Requires:       crate(%{pkgname}/nsarraycontroller) = %{version}
Requires:       crate(%{pkgname}/nsatstypesetter) = %{version}
Requires:       crate(%{pkgname}/nsattributedstring) = %{version}
Requires:       crate(%{pkgname}/nsbezierpath) = %{version}
Requires:       crate(%{pkgname}/nsbitmapimagerep) = %{version}
Requires:       crate(%{pkgname}/nsbox) = %{version}
Requires:       crate(%{pkgname}/nsbrowser) = %{version}
Requires:       crate(%{pkgname}/nsbrowsercell) = %{version}
Requires:       crate(%{pkgname}/nsbutton) = %{version}
Requires:       crate(%{pkgname}/nsbuttoncell) = %{version}
Requires:       crate(%{pkgname}/nsbuttontouchbaritem) = %{version}
Requires:       crate(%{pkgname}/nscachedimagerep) = %{version}
Requires:       crate(%{pkgname}/nscandidatelisttouchbaritem) = %{version}
Requires:       crate(%{pkgname}/nscell) = %{version}
Requires:       crate(%{pkgname}/nsciimagerep) = %{version}
Requires:       crate(%{pkgname}/nsclickgesturerecognizer) = %{version}
Requires:       crate(%{pkgname}/nsclipview) = %{version}
Requires:       crate(%{pkgname}/nscollectionview) = %{version}
Requires:       crate(%{pkgname}/nscollectionviewcompositionallayout) = %{version}
Requires:       crate(%{pkgname}/nscollectionviewflowlayout) = %{version}
Requires:       crate(%{pkgname}/nscollectionviewgridlayout) = %{version}
Requires:       crate(%{pkgname}/nscollectionviewlayout) = %{version}
Requires:       crate(%{pkgname}/nscollectionviewtransitionlayout) = %{version}
Requires:       crate(%{pkgname}/nscolor) = %{version}
Requires:       crate(%{pkgname}/nscolorlist) = %{version}
Requires:       crate(%{pkgname}/nscolorpanel) = %{version}
Requires:       crate(%{pkgname}/nscolorpicker) = %{version}
Requires:       crate(%{pkgname}/nscolorpickertouchbaritem) = %{version}
Requires:       crate(%{pkgname}/nscolorpicking) = %{version}
Requires:       crate(%{pkgname}/nscolorsampler) = %{version}
Requires:       crate(%{pkgname}/nscolorspace) = %{version}
Requires:       crate(%{pkgname}/nscolorwell) = %{version}
Requires:       crate(%{pkgname}/nscombobox) = %{version}
Requires:       crate(%{pkgname}/nscomboboxcell) = %{version}
Requires:       crate(%{pkgname}/nscombobutton) = %{version}
Requires:       crate(%{pkgname}/nscontrol) = %{version}
Requires:       crate(%{pkgname}/nscontroller) = %{version}
Requires:       crate(%{pkgname}/nscursor) = %{version}
Requires:       crate(%{pkgname}/nscustomimagerep) = %{version}
Requires:       crate(%{pkgname}/nscustomtouchbaritem) = %{version}
Requires:       crate(%{pkgname}/nsdataasset) = %{version}
Requires:       crate(%{pkgname}/nsdatepicker) = %{version}
Requires:       crate(%{pkgname}/nsdatepickercell) = %{version}
Requires:       crate(%{pkgname}/nsdictionarycontroller) = %{version}
Requires:       crate(%{pkgname}/nsdiffabledatasource) = %{version}
Requires:       crate(%{pkgname}/nsdocktile) = %{version}
Requires:       crate(%{pkgname}/nsdocument) = %{version}
Requires:       crate(%{pkgname}/nsdocumentcontroller) = %{version}
Requires:       crate(%{pkgname}/nsdocumentscripting) = %{version}
Requires:       crate(%{pkgname}/nsdragging) = %{version}
Requires:       crate(%{pkgname}/nsdraggingitem) = %{version}
Requires:       crate(%{pkgname}/nsdraggingsession) = %{version}
Requires:       crate(%{pkgname}/nsdrawer) = %{version}
Requires:       crate(%{pkgname}/nsepsimagerep) = %{version}
Requires:       crate(%{pkgname}/nserrors) = %{version}
Requires:       crate(%{pkgname}/nsevent) = %{version}
Requires:       crate(%{pkgname}/nsfilepromiseprovider) = %{version}
Requires:       crate(%{pkgname}/nsfilepromisereceiver) = %{version}
Requires:       crate(%{pkgname}/nsfilewrapperextensions) = %{version}
Requires:       crate(%{pkgname}/nsfont) = %{version}
Requires:       crate(%{pkgname}/nsfontassetrequest) = %{version}
Requires:       crate(%{pkgname}/nsfontcollection) = %{version}
Requires:       crate(%{pkgname}/nsfontdescriptor) = %{version}
Requires:       crate(%{pkgname}/nsfontmanager) = %{version}
Requires:       crate(%{pkgname}/nsfontpanel) = %{version}
Requires:       crate(%{pkgname}/nsform) = %{version}
Requires:       crate(%{pkgname}/nsformcell) = %{version}
Requires:       crate(%{pkgname}/nsgesturerecognizer) = %{version}
Requires:       crate(%{pkgname}/nsglyphgenerator) = %{version}
Requires:       crate(%{pkgname}/nsglyphinfo) = %{version}
Requires:       crate(%{pkgname}/nsgradient) = %{version}
Requires:       crate(%{pkgname}/nsgraphics) = %{version}
Requires:       crate(%{pkgname}/nsgraphicscontext) = %{version}
Requires:       crate(%{pkgname}/nsgridview) = %{version}
Requires:       crate(%{pkgname}/nsgrouptouchbaritem) = %{version}
Requires:       crate(%{pkgname}/nshapticfeedback) = %{version}
Requires:       crate(%{pkgname}/nshelpmanager) = %{version}
Requires:       crate(%{pkgname}/nsimage) = %{version}
Requires:       crate(%{pkgname}/nsimagecell) = %{version}
Requires:       crate(%{pkgname}/nsimagerep) = %{version}
Requires:       crate(%{pkgname}/nsimageview) = %{version}
Requires:       crate(%{pkgname}/nsinputmanager) = %{version}
Requires:       crate(%{pkgname}/nsinputserver) = %{version}
Requires:       crate(%{pkgname}/nsinterfacestyle) = %{version}
Requires:       crate(%{pkgname}/nsitemprovider) = %{version}
Requires:       crate(%{pkgname}/nskeyvaluebinding) = %{version}
Requires:       crate(%{pkgname}/nslayoutanchor) = %{version}
Requires:       crate(%{pkgname}/nslayoutconstraint) = %{version}
Requires:       crate(%{pkgname}/nslayoutguide) = %{version}
Requires:       crate(%{pkgname}/nslayoutmanager) = %{version}
Requires:       crate(%{pkgname}/nslevelindicator) = %{version}
Requires:       crate(%{pkgname}/nslevelindicatorcell) = %{version}
Requires:       crate(%{pkgname}/nsmagnificationgesturerecognizer) = %{version}
Requires:       crate(%{pkgname}/nsmatrix) = %{version}
Requires:       crate(%{pkgname}/nsmedialibrarybrowsercontroller) = %{version}
Requires:       crate(%{pkgname}/nsmenu) = %{version}
Requires:       crate(%{pkgname}/nsmenuitem) = %{version}
Requires:       crate(%{pkgname}/nsmenuitembadge) = %{version}
Requires:       crate(%{pkgname}/nsmenuitemcell) = %{version}
Requires:       crate(%{pkgname}/nsmenutoolbaritem) = %{version}
Requires:       crate(%{pkgname}/nsmovie) = %{version}
Requires:       crate(%{pkgname}/nsnib) = %{version}
Requires:       crate(%{pkgname}/nsnibdeclarations) = %{version}
Requires:       crate(%{pkgname}/nsnibloading) = %{version}
Requires:       crate(%{pkgname}/nsobjectcontroller) = %{version}
Requires:       crate(%{pkgname}/nsopengl) = %{version}
Requires:       crate(%{pkgname}/nsopengllayer) = %{version}
Requires:       crate(%{pkgname}/nsopenglview) = %{version}
Requires:       crate(%{pkgname}/nsopenpanel) = %{version}
Requires:       crate(%{pkgname}/nsoutlineview) = %{version}
Requires:       crate(%{pkgname}/nspagecontroller) = %{version}
Requires:       crate(%{pkgname}/nspagelayout) = %{version}
Requires:       crate(%{pkgname}/nspanel) = %{version}
Requires:       crate(%{pkgname}/nspangesturerecognizer) = %{version}
Requires:       crate(%{pkgname}/nsparagraphstyle) = %{version}
Requires:       crate(%{pkgname}/nspasteboard) = %{version}
Requires:       crate(%{pkgname}/nspasteboarditem) = %{version}
Requires:       crate(%{pkgname}/nspathcell) = %{version}
Requires:       crate(%{pkgname}/nspathcomponentcell) = %{version}
Requires:       crate(%{pkgname}/nspathcontrol) = %{version}
Requires:       crate(%{pkgname}/nspathcontrolitem) = %{version}
Requires:       crate(%{pkgname}/nspdfimagerep) = %{version}
Requires:       crate(%{pkgname}/nspdfinfo) = %{version}
Requires:       crate(%{pkgname}/nspdfpanel) = %{version}
Requires:       crate(%{pkgname}/nspersistentdocument) = %{version}
Requires:       crate(%{pkgname}/nspickertouchbaritem) = %{version}
Requires:       crate(%{pkgname}/nspictimagerep) = %{version}
Requires:       crate(%{pkgname}/nspopover) = %{version}
Requires:       crate(%{pkgname}/nspopovertouchbaritem) = %{version}
Requires:       crate(%{pkgname}/nspopupbutton) = %{version}
Requires:       crate(%{pkgname}/nspopupbuttoncell) = %{version}
Requires:       crate(%{pkgname}/nspredicateeditor) = %{version}
Requires:       crate(%{pkgname}/nspredicateeditorrowtemplate) = %{version}
Requires:       crate(%{pkgname}/nspressgesturerecognizer) = %{version}
Requires:       crate(%{pkgname}/nspressureconfiguration) = %{version}
Requires:       crate(%{pkgname}/nspreviewrepresentingactivityitem) = %{version}
Requires:       crate(%{pkgname}/nsprinter) = %{version}
Requires:       crate(%{pkgname}/nsprintinfo) = %{version}
Requires:       crate(%{pkgname}/nsprintoperation) = %{version}
Requires:       crate(%{pkgname}/nsprintpanel) = %{version}
Requires:       crate(%{pkgname}/nsprogressindicator) = %{version}
Requires:       crate(%{pkgname}/nsresponder) = %{version}
Requires:       crate(%{pkgname}/nsrotationgesturerecognizer) = %{version}
Requires:       crate(%{pkgname}/nsruleeditor) = %{version}
Requires:       crate(%{pkgname}/nsrulermarker) = %{version}
Requires:       crate(%{pkgname}/nsrulerview) = %{version}
Requires:       crate(%{pkgname}/nsrunningapplication) = %{version}
Requires:       crate(%{pkgname}/nssavepanel) = %{version}
Requires:       crate(%{pkgname}/nsscreen) = %{version}
Requires:       crate(%{pkgname}/nsscroller) = %{version}
Requires:       crate(%{pkgname}/nsscrollview) = %{version}
Requires:       crate(%{pkgname}/nsscrubber) = %{version}
Requires:       crate(%{pkgname}/nsscrubberitemview) = %{version}
Requires:       crate(%{pkgname}/nsscrubberlayout) = %{version}
Requires:       crate(%{pkgname}/nssearchfield) = %{version}
Requires:       crate(%{pkgname}/nssearchfieldcell) = %{version}
Requires:       crate(%{pkgname}/nssearchtoolbaritem) = %{version}
Requires:       crate(%{pkgname}/nssecuretextfield) = %{version}
Requires:       crate(%{pkgname}/nssegmentedcell) = %{version}
Requires:       crate(%{pkgname}/nssegmentedcontrol) = %{version}
Requires:       crate(%{pkgname}/nsshadow) = %{version}
Requires:       crate(%{pkgname}/nssharingservice) = %{version}
Requires:       crate(%{pkgname}/nssharingservicepickertoolbaritem) = %{version}
Requires:       crate(%{pkgname}/nssharingservicepickertouchbaritem) = %{version}
Requires:       crate(%{pkgname}/nsslider) = %{version}
Requires:       crate(%{pkgname}/nsslideraccessory) = %{version}
Requires:       crate(%{pkgname}/nsslidercell) = %{version}
Requires:       crate(%{pkgname}/nsslidertouchbaritem) = %{version}
Requires:       crate(%{pkgname}/nssound) = %{version}
Requires:       crate(%{pkgname}/nsspeechrecognizer) = %{version}
Requires:       crate(%{pkgname}/nsspeechsynthesizer) = %{version}
Requires:       crate(%{pkgname}/nsspellchecker) = %{version}
Requires:       crate(%{pkgname}/nsspellprotocol) = %{version}
Requires:       crate(%{pkgname}/nssplitview) = %{version}
Requires:       crate(%{pkgname}/nssplitviewcontroller) = %{version}
Requires:       crate(%{pkgname}/nssplitviewitem) = %{version}
Requires:       crate(%{pkgname}/nsstackview) = %{version}
Requires:       crate(%{pkgname}/nsstatusbar) = %{version}
Requires:       crate(%{pkgname}/nsstatusbarbutton) = %{version}
Requires:       crate(%{pkgname}/nsstatusitem) = %{version}
Requires:       crate(%{pkgname}/nsstepper) = %{version}
Requires:       crate(%{pkgname}/nssteppercell) = %{version}
Requires:       crate(%{pkgname}/nssteppertouchbaritem) = %{version}
Requires:       crate(%{pkgname}/nsstoryboard) = %{version}
Requires:       crate(%{pkgname}/nsstoryboardsegue) = %{version}
Requires:       crate(%{pkgname}/nsstringdrawing) = %{version}
Requires:       crate(%{pkgname}/nsswitch) = %{version}
Requires:       crate(%{pkgname}/nstablecellview) = %{version}
Requires:       crate(%{pkgname}/nstablecolumn) = %{version}
Requires:       crate(%{pkgname}/nstableheadercell) = %{version}
Requires:       crate(%{pkgname}/nstableheaderview) = %{version}
Requires:       crate(%{pkgname}/nstablerowview) = %{version}
Requires:       crate(%{pkgname}/nstableview) = %{version}
Requires:       crate(%{pkgname}/nstableviewdiffabledatasource) = %{version}
Requires:       crate(%{pkgname}/nstableviewrowaction) = %{version}
Requires:       crate(%{pkgname}/nstabview) = %{version}
Requires:       crate(%{pkgname}/nstabviewcontroller) = %{version}
Requires:       crate(%{pkgname}/nstabviewitem) = %{version}
Requires:       crate(%{pkgname}/nstext) = %{version}
Requires:       crate(%{pkgname}/nstextalternatives) = %{version}
Requires:       crate(%{pkgname}/nstextattachment) = %{version}
Requires:       crate(%{pkgname}/nstextattachmentcell) = %{version}
Requires:       crate(%{pkgname}/nstextcheckingclient) = %{version}
Requires:       crate(%{pkgname}/nstextcheckingcontroller) = %{version}
Requires:       crate(%{pkgname}/nstextcontainer) = %{version}
Requires:       crate(%{pkgname}/nstextcontent) = %{version}
Requires:       crate(%{pkgname}/nstextcontentmanager) = %{version}
Requires:       crate(%{pkgname}/nstextelement) = %{version}
Requires:       crate(%{pkgname}/nstextfield) = %{version}
Requires:       crate(%{pkgname}/nstextfieldcell) = %{version}
Requires:       crate(%{pkgname}/nstextfinder) = %{version}
Requires:       crate(%{pkgname}/nstextinputclient) = %{version}
Requires:       crate(%{pkgname}/nstextinputcontext) = %{version}
Requires:       crate(%{pkgname}/nstextinsertionindicator) = %{version}
Requires:       crate(%{pkgname}/nstextlayoutfragment) = %{version}
Requires:       crate(%{pkgname}/nstextlayoutmanager) = %{version}
Requires:       crate(%{pkgname}/nstextlinefragment) = %{version}
Requires:       crate(%{pkgname}/nstextlist) = %{version}
Requires:       crate(%{pkgname}/nstextlistelement) = %{version}
Requires:       crate(%{pkgname}/nstextrange) = %{version}
Requires:       crate(%{pkgname}/nstextselection) = %{version}
Requires:       crate(%{pkgname}/nstextselectionnavigation) = %{version}
Requires:       crate(%{pkgname}/nstextstorage) = %{version}
Requires:       crate(%{pkgname}/nstextstoragescripting) = %{version}
Requires:       crate(%{pkgname}/nstexttable) = %{version}
Requires:       crate(%{pkgname}/nstextview) = %{version}
Requires:       crate(%{pkgname}/nstextviewportlayoutcontroller) = %{version}
Requires:       crate(%{pkgname}/nstintconfiguration) = %{version}
Requires:       crate(%{pkgname}/nstitlebaraccessoryviewcontroller) = %{version}
Requires:       crate(%{pkgname}/nstokenfield) = %{version}
Requires:       crate(%{pkgname}/nstokenfieldcell) = %{version}
Requires:       crate(%{pkgname}/nstoolbar) = %{version}
Requires:       crate(%{pkgname}/nstoolbaritem) = %{version}
Requires:       crate(%{pkgname}/nstoolbaritemgroup) = %{version}
Requires:       crate(%{pkgname}/nstouch) = %{version}
Requires:       crate(%{pkgname}/nstouchbar) = %{version}
Requires:       crate(%{pkgname}/nstouchbaritem) = %{version}
Requires:       crate(%{pkgname}/nstrackingarea) = %{version}
Requires:       crate(%{pkgname}/nstrackingseparatortoolbaritem) = %{version}
Requires:       crate(%{pkgname}/nstreecontroller) = %{version}
Requires:       crate(%{pkgname}/nstreenode) = %{version}
Requires:       crate(%{pkgname}/nstypesetter) = %{version}
Requires:       crate(%{pkgname}/nsuseractivity) = %{version}
Requires:       crate(%{pkgname}/nsuserdefaultscontroller) = %{version}
Requires:       crate(%{pkgname}/nsuserinterfacecompression) = %{version}
Requires:       crate(%{pkgname}/nsuserinterfaceitemidentification) = %{version}
Requires:       crate(%{pkgname}/nsuserinterfaceitemsearching) = %{version}
Requires:       crate(%{pkgname}/nsuserinterfacelayout) = %{version}
Requires:       crate(%{pkgname}/nsuserinterfacevalidation) = %{version}
Requires:       crate(%{pkgname}/nsview) = %{version}
Requires:       crate(%{pkgname}/nsviewcontroller) = %{version}
Requires:       crate(%{pkgname}/nsvisualeffectview) = %{version}
Requires:       crate(%{pkgname}/nswindow) = %{version}
Requires:       crate(%{pkgname}/nswindowcontroller) = %{version}
Requires:       crate(%{pkgname}/nswindowrestoration) = %{version}
Requires:       crate(%{pkgname}/nswindowscripting) = %{version}
Requires:       crate(%{pkgname}/nswindowtab) = %{version}
Requires:       crate(%{pkgname}/nswindowtabgroup) = %{version}
Requires:       crate(%{pkgname}/nsworkspace) = %{version}
Requires:       crate(%{pkgname}/objc2-core-data) = %{version}
Requires:       crate(%{pkgname}/objc2-core-image) = %{version}
Requires:       crate(%{pkgname}/objc2-quartz-core) = %{version}
Provides:       crate(%{pkgname}/all) = %{version}

%description -n %{name}+all
This metapackage enables feature "all" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+alloc
Summary:        Bindings to the AppKit framework - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(block2-0.5/alloc) >= 0.5.1
Requires:       crate(objc2-0.5/alloc) >= 0.5.2
Requires:       crate(objc2-core-data-0.2/alloc) >= 0.2.2
Requires:       crate(objc2-core-image-0.2/alloc) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/alloc) >= 0.2.2
Requires:       crate(objc2-quartz-core-0.2/alloc) >= 0.2.2
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bitflags
Summary:        Bindings to the AppKit framework - feature "bitflags"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bitflags-2) >= 2.5.0
Requires:       crate(objc2-core-data-0.2/bitflags) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/bitflags) >= 0.2.2
Requires:       crate(objc2-quartz-core-0.2/bitflags) >= 0.2.2
Provides:       crate(%{pkgname}/bitflags) = %{version}

%description -n %{name}+bitflags
This metapackage enables feature "bitflags" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+block2
Summary:        Bindings to the AppKit framework - feature "block2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(block2-0.5) >= 0.5.1
Requires:       crate(objc2-core-data-0.2/block2) >= 0.2.2
Requires:       crate(objc2-core-image-0.2/block2) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/block2) >= 0.2.2
Requires:       crate(objc2-quartz-core-0.2/block2) >= 0.2.2
Provides:       crate(%{pkgname}/block2) = %{version}

%description -n %{name}+block2
This metapackage enables feature "block2" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gnustep-1-7
Summary:        Bindings to the AppKit framework - feature "gnustep-1-7"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(block2-0.5/gnustep-1-7) >= 0.5.1
Requires:       crate(objc2-0.5/gnustep-1-7) >= 0.5.2
Requires:       crate(objc2-core-data-0.2/gnustep-1-7) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/gnustep-1-7) >= 0.2.2
Requires:       crate(objc2-quartz-core-0.2/gnustep-1-7) >= 0.2.2
Provides:       crate(%{pkgname}/gnustep-1-7) = %{version}

%description -n %{name}+gnustep-1-7
This metapackage enables feature "gnustep-1-7" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gnustep-1-8
Summary:        Bindings to the AppKit framework - feature "gnustep-1-8"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/gnustep-1-7) = %{version}
Requires:       crate(block2-0.5/gnustep-1-8) >= 0.5.1
Requires:       crate(objc2-0.5/gnustep-1-8) >= 0.5.2
Requires:       crate(objc2-core-data-0.2/gnustep-1-8) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/gnustep-1-8) >= 0.2.2
Requires:       crate(objc2-quartz-core-0.2/gnustep-1-8) >= 0.2.2
Provides:       crate(%{pkgname}/gnustep-1-8) = %{version}

%description -n %{name}+gnustep-1-8
This metapackage enables feature "gnustep-1-8" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gnustep-1-9
Summary:        Bindings to the AppKit framework - feature "gnustep-1-9"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/gnustep-1-8) = %{version}
Requires:       crate(block2-0.5/gnustep-1-9) >= 0.5.1
Requires:       crate(objc2-0.5/gnustep-1-9) >= 0.5.2
Requires:       crate(objc2-core-data-0.2/gnustep-1-9) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/gnustep-1-9) >= 0.2.2
Requires:       crate(objc2-quartz-core-0.2/gnustep-1-9) >= 0.2.2
Provides:       crate(%{pkgname}/gnustep-1-9) = %{version}

%description -n %{name}+gnustep-1-9
This metapackage enables feature "gnustep-1-9" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gnustep-2-0
Summary:        Bindings to the AppKit framework - feature "gnustep-2-0"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/gnustep-1-9) = %{version}
Requires:       crate(block2-0.5/gnustep-2-0) >= 0.5.1
Requires:       crate(objc2-0.5/gnustep-2-0) >= 0.5.2
Requires:       crate(objc2-core-data-0.2/gnustep-2-0) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/gnustep-2-0) >= 0.2.2
Requires:       crate(objc2-quartz-core-0.2/gnustep-2-0) >= 0.2.2
Provides:       crate(%{pkgname}/gnustep-2-0) = %{version}

%description -n %{name}+gnustep-2-0
This metapackage enables feature "gnustep-2-0" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+gnustep-2-1
Summary:        Bindings to the AppKit framework - feature "gnustep-2-1"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/gnustep-2-0) = %{version}
Requires:       crate(block2-0.5/gnustep-2-1) >= 0.5.1
Requires:       crate(objc2-0.5/gnustep-2-1) >= 0.5.2
Requires:       crate(objc2-core-data-0.2/gnustep-2-1) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/gnustep-2-1) >= 0.2.2
Requires:       crate(objc2-quartz-core-0.2/gnustep-2-1) >= 0.2.2
Provides:       crate(%{pkgname}/gnustep-2-1) = %{version}

%description -n %{name}+gnustep-2-1
This metapackage enables feature "gnustep-2-1" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libc
Summary:        Bindings to the AppKit framework - feature "libc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libc-0.2) >= 0.2.80
Requires:       crate(objc2-foundation-0.2/libc) >= 0.2.2
Provides:       crate(%{pkgname}/libc) = %{version}

%description -n %{name}+libc
This metapackage enables feature "libc" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-core-data
Summary:        Bindings to the AppKit framework - feature "objc2-core-data"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-core-data-0.2) >= 0.2.2
Provides:       crate(%{pkgname}/objc2-core-data) = %{version}

%description -n %{name}+objc2-core-data
This metapackage enables feature "objc2-core-data" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-core-image
Summary:        Bindings to the AppKit framework - feature "objc2-core-image"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-core-image-0.2) >= 0.2.2
Provides:       crate(%{pkgname}/objc2-core-image) = %{version}

%description -n %{name}+objc2-core-image
This metapackage enables feature "objc2-core-image" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-quartz-core
Summary:        Bindings to the AppKit framework - feature "objc2-quartz-core"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-quartz-core-0.2) >= 0.2.2
Provides:       crate(%{pkgname}/objc2-quartz-core) = %{version}

%description -n %{name}+objc2-quartz-core
This metapackage enables feature "objc2-quartz-core" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Bindings to the AppKit framework - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(bitflags-2/std) >= 2.5.0
Requires:       crate(block2-0.5/std) >= 0.5.1
Requires:       crate(libc-0.2/std) >= 0.2.80
Requires:       crate(objc2-0.5/std) >= 0.5.2
Requires:       crate(objc2-core-data-0.2/std) >= 0.2.2
Requires:       crate(objc2-core-image-0.2/std) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/std) >= 0.2.2
Requires:       crate(objc2-quartz-core-0.2/std) >= 0.2.2
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust objc2-app-kit crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog
