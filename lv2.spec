# "Clean files" deletes "core dump" files, such as
# %{_includedir}/lv2/core...
%global dont_clean_files 1

Name:		lv2
Version:	1.18.10
Release:	2
Summary:	Audio Plugin Standard
Group:		System/Libraries

# lv2specgen template.html is CC-AT-SA
License:	ISC
URL:		https://lv2plug.in
Source0:	http://lv2plug.in/spec/lv2-%{version}.tar.xz
Source1:	lv2.rpmlintrc

# For eg-sampler and eg-scope plugins -- safe to remove if we remove that sample plugin
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  python%{pyver}dist(black)
BuildRequires:  python%{pyver}dist(rdflib)
BuildRequires:  python%{pyver}dist(lxml)
BuildRequires:  python%{pyver}dist(markdown)
BuildRequires:  python%{pyver}dist(pygments)
BuildRequires:  python%{pyver}dist(codespell)
BuildRequires:  python%{pyver}dist(flake8)
BuildRequires:  python%{pyver}dist(pylint)
BuildRequires:  asciidoc
BuildRequires:  doxygen
BuildRequires:  meson
BuildRequires:  serd
BuildRequires:  sord

# this package replaces lv2core
Provides:	lv2core = 6.0-4
Obsoletes:	lv2core < 6.0-4
Provides:	lv2-ui = 2.4-5
Obsoletes:	lv2-ui < 2.4-5

BuildSystem:	meson

%description
LV2 is a standard for plugins and matching host applications, mainly
targeted at audio processing and generation.

There are a large number of open source and free software synthesis
packages in use or development at this time. This API ('LV2') attempts
to give programmers the ability to write simple 'plugin' audio
processors in C/C++ and link them dynamically ('plug') into a range of
these packages ('hosts').  It should be possible for any host and any
plugin to communicate completely through this interface.

LV2 is a successor to LADSPA, created to address the limitations of
LADSPA which many hosts have outgrown.

%package devel
Summary:	API for the LV2 Audio Plugin Standard
Group:		Development/C

Requires:	%{name} = %{EVRD}
Provides:	lv2core-devel = %{EVRD}
Provides:	lv2-ui-devel = %{EVRD}

BuildRequires:	pkgconfig(sndfile) >= 1.0.0

%description devel
lv2-devel contains the lv2.h header file and headers for all of the
LV@ specification extensions and bundles.

Definitive technical documentation on LV2 plug-ins for both the host
and plug-in is contained within copious comments within the lv2.h
header file.

%package plugins
Summary:	Sample plugins for LV2
Group:		System/Libraries
Requires:	%{name} = %{EVRD}
Requires:	%{name}-plugin-eg-amp = %{EVRD}
Requires:	%{name}-plugin-eg-fifths = %{EVRD}
Requires:	%{name}-plugin-eg-metro = %{EVRD}
Requires:	%{name}-plugin-eg-midigate = %{EVRD}
Requires:	%{name}-plugin-eg-params = %{EVRD}
Suggests:	%{name}-plugin-eg-sampler = %{EVRD}
Suggests:	%{name}-plugin-eg-scope = %{EVRD}

%description plugins
Sample plugins for LV2.

%package plugin-eg-amp
Summary:	Amp sample plugin for LV2
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description plugin-eg-amp
Amp sample plugins for LV2.

%package plugin-eg-fifths
Summary:	Fifths sample plugin for LV2
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description plugin-eg-fifths
Fifths sample plugins for LV2.

%package plugin-eg-metro
Summary:	Metronome sample plugin for LV2
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description plugin-eg-metro
Metronome sample plugins for LV2.

%package plugin-eg-midigate
Summary:	MIDI-Gate sample plugin for LV2
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description plugin-eg-midigate
MIDI-Gate sample plugins for LV2.

%package plugin-eg-params
Summary:	Params sample plugin for LV2
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description plugin-eg-params
Params sample plugins for LV2.

%package plugin-eg-sampler
Summary:	Sampler sample plugin for LV2
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description plugin-eg-sampler
Sampler sample plugins for LV2.

%package plugin-eg-scope
Summary:	Scope sample plugin for LV2
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description plugin-eg-scope
Scope sample plugins for LV2.

%install -a
# For compatibility with old releases
ln -s lv2.pc %{buildroot}%{_libdir}/pkgconfig/lv2core.pc

%files
%{_bindir}/lv2_validate
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/atom.lv2
%{_libdir}/%{name}/buf-size.lv2
%{_libdir}/%{name}/core.lv2
%{_libdir}/%{name}/data-access.lv2
%{_libdir}/%{name}/dynmanifest.lv2
%{_libdir}/%{name}/event.lv2
%{_libdir}/%{name}/instance-access.lv2
%{_libdir}/%{name}/log.lv2
%{_libdir}/%{name}/midi.lv2
%{_libdir}/%{name}/morph.lv2
%{_libdir}/%{name}/options.lv2
%{_libdir}/%{name}/parameters.lv2
%{_libdir}/%{name}/patch.lv2
%{_libdir}/%{name}/port-groups.lv2
%{_libdir}/%{name}/port-props.lv2
%{_libdir}/%{name}/presets.lv2
%{_libdir}/%{name}/resize-port.lv2
%{_libdir}/%{name}/schemas.lv2
%{_libdir}/%{name}/state.lv2
%{_libdir}/%{name}/time.lv2
%{_libdir}/%{name}/ui.lv2
%{_libdir}/%{name}/units.lv2
%{_libdir}/%{name}/urid.lv2
%{_libdir}/%{name}/uri-map.lv2
%{_libdir}/%{name}/worker.lv2

%files devel
%doc COPYING NEWS
%doc %{_datadir}/doc/lv2/
%{_bindir}/lv2specgen.py
%{_includedir}/%{name}/
%{_includedir}/lv2.h
%{_datadir}/lv2specgen/
%{_libdir}/pkgconfig/lv2core.pc
%{_libdir}/pkgconfig/%{name}.pc

%files plugins
# Empty legacy package, just pulls in the split-out plugins

%files plugin-eg-amp
%{_libdir}/%{name}/eg-amp.lv2

%files plugin-eg-fifths
%{_libdir}/%{name}/eg-fifths.lv2

%files plugin-eg-metro
%{_libdir}/%{name}/eg-metro.lv2

%files plugin-eg-midigate
%{_libdir}/%{name}/eg-midigate.lv2

%files plugin-eg-params
%{_libdir}/%{name}/eg-params.lv2

%files plugin-eg-sampler
%{_libdir}/%{name}/eg-sampler.lv2

%files plugin-eg-scope
%{_libdir}/%{name}/eg-scope.lv2
